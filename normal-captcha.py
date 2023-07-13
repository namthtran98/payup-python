from twocaptcha import TwoCaptcha
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from solveRecapcha import solveRecapcha
from solveClickCapcha import solveClickCapcha
from solveClickCapcha import giai_captcha
from solveClickCapcha import take_image
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import re
import requests
import json
from time import sleep
import re
import undetected_chromedriver as uc

if __name__ == '__main__':
    us = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    apikey = "o8EPL80Zhhp0RX7eu4fcYkVxoL5nci42"
    browser = uc.Chrome()
    browser.maximize_window()
    browser.get('https://payup.video/signin/')
    txtboxUsername = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Enter your email']")
    txtboxUsername.send_keys("awsnamtran01@gmail.com")
    txtboxPassword = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Set your password']")
    txtboxPassword.send_keys("Sinhnam1998")
    # recaptcha
    result = solveRecapcha(
        "6LccP4klAAAAAOZUvkGg5n_nam1GMaege6EJDGf4",
        "https://payup.video/signin/"
    )
    code = result['code']
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
    )

    browser.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")

    btnSignUp = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("arguments[0].click();", btnSignUp)
    time.sleep(10)
    i = True
    while i == True:
        window_before = browser.window_handles[0]
        browser.switch_to.window(window_before)
        tabEarning = browser.find_element(
            By.CSS_SELECTOR, ".btn.btn-light-success.bg-transparent.px-0.d-flex.align-items-center.font-weight-bolder")
        browser.execute_script("arguments[0].click();", tabEarning)
        time.sleep(15)
        all_cookies = browser.get_cookies()
        cookies_dict = {}
        for cookie in all_cookies:
            cookies_dict[cookie['name']] = cookie['value']
        cookie1 = "_ga=" + cookies_dict['_ga'] + "; " + "_ym_d=" + cookies_dict['_ym_d'] + "; " + "_ym_uid=" + cookies_dict["_ym_uid"] + "; " + "newUser=1" + "; " + "PHPSESSID=" + cookies_dict["PHPSESSID"] + "; " + \
            "signed=" + cookies_dict["signed"] + "; " + "_ym_isad=" + cookies_dict["_ym_isad"] + "; " + "_ym_visorc=" + \
            cookies_dict["_ym_visorc"] + "; " + "hash=" + cookies_dict["hash"] + \
            "; " + "_ga_5JGWQMNX26=" + cookies_dict["_ga_5JGWQMNX26"]
        btnviewVideo = browser.find_elements(By.CSS_SELECTOR, "#btn_card_run")
        if btnviewVideo:
            btnviewVideo[0].click()
            time.sleep(10)
            window_after = browser.window_handles[1]
            browser.switch_to.window(window_after)

            browser._switch_to.frame(browser.find_element(
                By.XPATH, "//iframe"))
            btnPlay = browser.find_element(
                By.XPATH, "//button[@class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg']")
            btnPlay.click()
            browser.switch_to.default_content()
            spanTimer = browser.find_element(By.CSS_SELECTOR, "#timer")
            timeSleep = int(spanTimer.text)
            time.sleep(timeSleep + 6)
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#captcha')))
        element = browser.find_element(By.CSS_SELECTOR, "#captcha")
        if element.is_displayed():
            headers = {
                'authority': 'payup.video',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': cookie1,
                'origin': 'https://payup.video',
                'referer': 'https://payup.video/tasks/video/',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': us,
            }

            data = {
                'type': 'video',
            }
            response = requests.post(
                'https://payup.video/tasks/control/get.php', headers=headers, data=data).text
            response_dict = json.loads(response)
            data3 = response_dict['data']
            s_id = response_dict['data']['s_id']
            id = response_dict['data']['id']
            headers2 = {
                'authority': 'payup.video',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://trustspace.squarespace.com',
                'referer': 'https://trustspace.squarespace.com/',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': us,
            }

            data2 = {
                's_id': s_id,
                'id': id
            }

            response2 = requests.post(
                'https://payup.video/captcha/control/get.php', headers=headers2, data=data2)
            if response2.status_code == 200:
                rs_load = response2.json()
                co_captcha_khong = rs_load['status']
            if "OK" == co_captcha_khong:
                    print('dinh captcha')
                    body = rs_load['data']
                    g = giai_captcha(apikey=apikey, body=body,
                                     s_id=s_id, headers2=headers2)

                    # if response5.status_code == 200:
                    #     print('giai captcha thanh cong')
                    # else:
                    #     return "GIAI CAPTCHA LOI"

                else:
                    headers = {
                        'authority': 'payup.video',
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'origin': 'https://trustspace.squarespace.com',
                        'referer': 'https://trustspace.squarespace.com/',
                        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'cross-site',
                        'user-agent': us,
                    }

                    data = {
                        's_id': s_id,
                    }

                    response3 = requests.post(
                        'https://payup.video/captcha/control/check.php', headers=headers, data=data)

                    print(response3)

            # action = ActionChains(browser)
            # action.move_to_element_with_offset(
            #    element, float[coordinates[0]], float(coordinates[1])).click().perform()
            # print(result['code'])
            # print(element.location)
            time.sleep(5)
        # wpyautogui.hotkey("command", "w", interval=0.5)
        browser.close()
