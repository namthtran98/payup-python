from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import SolveRecaptcha
import time
from SolveBuxMoneyCaptcha import SolveBuxMoneyCaptcha


def Buxmoney(buxusername, buxpassword, apikey):
    browser = uc.Chrome()
    timeWaitElement = 60
    browser.implicitly_wait(30)
    browser.get("https://bux.money/signin/")
    us = browser.execute_script("return navigator.userAgent;")
    username = browser.find_element(By.ID, "email")
    username.send_keys(buxusername)
    password = browser.find_element(By.ID, "password")
    password.send_keys(buxpassword)
    result = SolveRecaptcha.TGSolveCaptcha(
        "6LeGu9wZAAAAAPrFSfn4hLNNxf0bCnLLLtfdIRo5", "https://bux.money/signin/", "o8EPL80Zhhp0RX7eu4fcYkVxoL5nci42")
    WebDriverWait(browser, timeWaitElement).until(
        EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
    )
    browser.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + result + "'")
    btnSubmit = browser.find_element(By.XPATH, "//input[@type='submit']")
    btnSubmit.click()
    dropdown = browser.find_element(By.CSS_SELECTOR, "#desktop-hs a")
    dropdown.click()
    userDropdown = browser.find_element(
        By.XPATH, "//div[@id='desktop-hs']//span[@data-type='user']")
    userDropdown.click()
    tabYoutube = browser.find_element(
        By.XPATH, "//div[@class='d-none d-xl-flex new-header-bot']//a[@href='/tasks/video/']")
    tabYoutube.click()
    x = True
    while x == True:
        window_before = browser.window_handles[0]
        browser.switch_to.window(window_before)
        browser.refresh()
        WebDriverWait(browser, timeWaitElement).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#btn_card_run")))
        curlLimit = int(browser.find_element(
            By.CSS_SELECTOR, "#curLimit").text)
        allLimit = int(browser.find_element(By.CSS_SELECTOR, "#allLimit").text)
        if (curlLimit == 0 and allLimit == 0):
            x = False
        elif (curlLimit > 0 or allLimit > 0):
            all_cookies = browser.get_cookies()
            cookies_dict = {}
            for cookie in all_cookies:
                cookies_dict[cookie['name']] = cookie['value']
            cookie1 = "hash=" + cookies_dict['hash'] + ";" +\
                "signed=" + cookies_dict['signed'] + ";" + \
                "_ym_uid=" + cookies_dict['_ym_uid'] + ";" + \
                "_ym_d=" + cookies_dict['_ym_d'] + ";" + \
                "page=" + cookies_dict['page'] + ";" + \
                "_ym_isad=" + cookies_dict['_ym_isad'] + ";" + \
                "_ym_visorc=" + cookies_dict['_ym_visorc'] + ";" + \
                "PHPSESSID=" + cookies_dict['PHPSESSID']
            btnViewVideo = browser.find_element(
                By.CSS_SELECTOR, "#btn_card_run")
            btnViewVideo.click()
            window_after = browser.window_handles[1]
            browser.switch_to.window(window_after)
            try:
                WebDriverWait(browser, timeWaitElement).until(
                    EC.visibility_of_element_located((By.XPATH, "//iframe")))
                iframe = browser.find_element(By.XPATH, "//iframe")
                browser._switch_to.frame(iframe)
                btnPlay = browser.find_element(
                    By.XPATH, "//button[@class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg']")
                btnPlay.click()
            except:
                z = False
                while z == False:
                    browser.close()
                    browser.switch_to.window(window_before)
                    tabYoutube = browser.find_element(
                        By.XPATH, "//div[@class='d-none d-xl-flex new-header-bot']//a[@href='/tasks/video/']")
                    tabYoutube.click()
                    WebDriverWait(browser, timeWaitElement).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn_card_run")))
                    btnviewVideo = browser.find_elements(
                        By.CSS_SELECTOR, "#btn_card_run")
                    btnviewVideo[0].click()
                    window_after = browser.window_handles[1]
                    browser.switch_to.window(window_after)
                    try:
                        WebDriverWait(browser, timeWaitElement).until(
                            EC.presence_of_element_located((By.XPATH, "//iframe")))
                        iframe = browser.find_element(By.XPATH, "//iframe")
                        browser._switch_to.frame(iframe)
                        btnPlay = browser.find_element(
                            By.XPATH, "//button[@class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg']")
                        btnPlay.click()
                        z = True
                    except:
                        continue
            browser.switch_to.default_content()
            spanTimer = browser.find_element(By.CSS_SELECTOR, "#timer")
            timeSleep = int(spanTimer.text)
            try:
                WebDriverWait(browser, timeSleep).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='status-bar-text']//span")))
                WebDriverWait(browser, timeWaitElement).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#captcha')))
                element = browser.find_element(By.CSS_SELECTOR, "#captcha")
            except:
                WebDriverWait(browser, timeWaitElement).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#captcha')))
                element = browser.find_element(By.CSS_SELECTOR, "#captcha")
            if element.is_displayed():
                SolveBuxMoneyCaptcha(us, apikey, cookie1)
        browser.close()
