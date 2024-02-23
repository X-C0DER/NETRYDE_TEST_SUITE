import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def logged_in_browser(browser):
    browser.get("https://dev-np.netryde.com/")
    browser.set_window_size(1366, 728)
    browser.find_element(By.ID, "Log inTextArea").click()
    browser.find_element(By.LINK_TEXT, "Login as a Customer").click()
    browser.find_element(By.ID, "1").send_keys("nrct2@zprodev.com")
    browser.find_element(By.ID, "3").send_keys("Test@123")
    browser.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
    browser.find_element(By.CSS_SELECTOR, ".auth-form").click()
    browser.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    time.sleep(5)
    yield browser

class TestE2ECustomerLogin:
    def test_login(self, logged_in_browser):
        browser = logged_in_browser
        browser.find_element(By.CSS_SELECTOR, ".\\_nav-links_1xe3h_48 h1").click()
        time.sleep(2)
        assert browser.find_element(By.CSS_SELECTOR, ".\\_user-menu-logout-btn_1xe3h_219").text == "Logout"

    def test_logout(self, logged_in_browser):
        browser = logged_in_browser
        logout_btn=browser.find_element(By.CSS_SELECTOR, ".\\_user-menu-logout-btn_1xe3h_219")
        logout_btn.click()
        time.sleep(3)
        assert 'NetRyde' in browser.title

