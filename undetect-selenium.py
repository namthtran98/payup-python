from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

if __name__ == '__main__':
    browser = uc.Chrome()
    browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    browser.find_element(By.CSS_SELECTOR, "#identifierId").send_keys(
        'tranthanhnam.tpqn@gmail.com')
    browser.find_element(
        By.CSS_SELECTOR, "#identifierNext > div > button > span").click()
    password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, password_selector))
    )
    browser.find_element(
        By.CSS_SELECTOR, password_selector).send_keys("Sinhnam1998")
    browser.find_element(
        By.CSS_SELECTOR, "#passwordNext > div > button > div.VfPpkd-RLmnJb").click()
browser
