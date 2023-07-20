from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import solveRecapcha
from SolvePayupCaptcha import SolvePayupCaptcha
import time
import undetected_chromedriver as uc


if __name__ == '__main__':
    apikey = "o8EPL80Zhhp0RX7eu4fcYkVxoL5nci42"
    browser = uc.Chrome()
    browser.maximize_window()
    browser.get('https://payup.video/signin/')
    us = browser.execute_script("return navigator.userAgent;")
    txtboxUsername = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Enter your email']")
    txtboxUsername.send_keys("#")
    txtboxPassword = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Set your password']")
    txtboxPassword.send_keys("#")
    result = solveRecapcha.TGSolveCaptcha(
        "6LccP4klAAAAAOZUvkGg5n_nam1GMaege6EJDGf4", "https://payup.video/signin/", apikey)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
    )

    browser.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + result + "'")
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, "//h2")))
    btnSignUp = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("arguments[0].click();", btnSignUp)
    WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-light-success.bg-transparent.px-0.d-flex.align-items-center.font-weight-bolder")))
    while True:
        window_before = browser.window_handles[0]
        browser.switch_to.window(window_before)
        tabEarning = browser.find_element(
            By.CSS_SELECTOR, ".btn.btn-light-success.bg-transparent.px-0.d-flex.align-items-center.font-weight-bolder")
        browser.execute_script("arguments[0].click();", tabEarning)
        WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn_card_run")))
        curLimit = int(browser.find_element(By.CSS_SELECTOR, "#curLimit").text)
        allLimit = int(browser.find_element(By.CSS_SELECTOR, "#allLimit").text)
        if curLimit > 0 or allLimit > 0:
            all_cookies = browser.get_cookies()
            cookies_dict = {}
            for cookie in all_cookies:
                cookies_dict[cookie['name']] = cookie['value']
            cookie1 = "_ga=" + cookies_dict['_ga'] + "; " + "_ym_d=" + cookies_dict['_ym_d'] + "; " + "_ym_uid=" + cookies_dict["_ym_uid"] + "; " + "newUser=1" + "; " + "PHPSESSID=" + cookies_dict["PHPSESSID"] + "; " + \
                "signed=" + cookies_dict["signed"] + "; " + "_ym_isad=" + cookies_dict["_ym_isad"] + "; " + "_ym_visorc=" + \
                cookies_dict["_ym_visorc"] + "; " + "hash=" + cookies_dict["hash"] + \
                "; " + "_ga_5JGWQMNX26=" + cookies_dict["_ga_5JGWQMNX26"]
        elif curLimit == 0 and allLimit == 0:
            time.sleep(3600000)
            continue
        btnviewVideo = browser.find_elements(By.CSS_SELECTOR, "#btn_card_run")
        if btnviewVideo:
            btnviewVideo[0].click()
            window_after = browser.window_handles[1]
            browser.switch_to.window(window_after)
            try:
                WebDriverWait(browser, 15).until(
                    EC.visibility_of_element_located((By.XPATH, "//iframe")))
                iframe = browser.find_element(By.XPATH, "//iframe")
                browser._switch_to.frame(iframe)
                btnPlay = browser.find_element(
                    By.XPATH, "//button[@class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg']")
                btnPlay.click()
            except:
                i = False
                while i == False:
                    browser.close()
                    browser.switch_to.window(window_before)
                    tabEarning = browser.find_element(
                        By.CSS_SELECTOR, ".btn.btn-light-success.bg-transparent.px-0.d-flex.align-items-center.font-weight-bolder")
                    tabEarning.click()
                    WebDriverWait(browser, 15).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn_card_run")))
                    btnviewVideo[0].click()
                    WebDriverWait(browser, 15).until(
                        EC.visibility_of_element_located((By.XPATH, "//iframe")))
                    window_after = browser.window_handles[1]
                    browser.switch_to.window(window_after)
                    try:
                        WebDriverWait(browser, 30).until(
                            EC.presence_of_element_located((By.XPATH, "//iframe")))
                        iframe = browser.find_element(By.XPATH, "//iframe")
                        browser._switch_to.frame(iframe)
                        btnPlay = browser.find_element(
                            By.XPATH, "//button[@class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg']")
                        btnPlay.click()
                        i = True
                    except:
                        continue
            browser.switch_to.default_content()
            spanTimer = browser.find_element(By.CSS_SELECTOR, "#timer")
            timeSleep = int(spanTimer.text)
            try:
                WebDriverWait(browser, timeSleep + 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='status-bar-text']//span")))
                WebDriverWait(browser, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#captcha')))
                element = browser.find_element(By.CSS_SELECTOR, "#captcha")
            except:
                WebDriverWait(browser, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#captcha')))
                element = browser.find_element(By.CSS_SELECTOR, "#captcha")
        if element.is_displayed():
            SolvePayupCaptcha(us, apikey, cookie1)
        browser.close()
