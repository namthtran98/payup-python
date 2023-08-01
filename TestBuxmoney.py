from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SolveRecaptcha
from SolvePayupCaptcha import SolvePayupCaptcha
from ReadFile import ReadFile
import time
import undetected_chromedriver as uc
from Buxmoney import Buxmoney

if __name__ == '__main__':
    data = ReadFile()
    username = data['username']
    password = data['password']
    apikey = data['apikey']
    buxusername = data['buxusername']
    buxpassword = data['buxpassword']
    browser = uc.Chrome()
    browser.maximize_window()
    x = True
    while x == True:
        x = Buxmoney(browser, x, apikey, buxusername, buxpassword)
