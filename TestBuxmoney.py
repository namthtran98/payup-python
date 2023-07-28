from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SolveRecapcha
from SolvePayupCaptcha import SolvePayupCaptcha
from ReadFile import ReadFile
import time
import undetected_chromedriver as uc
from Buxmoney import Buxmoney

if __name__ == '__main__':
    browser = uc.Chrome()
    browser.maximize_window()
    i = True
    x = Buxmoney(browser=browser, i=i,
                 apikey="o8EPL80Zhhp0RX7eu4fcYkVxoL5nci42")
