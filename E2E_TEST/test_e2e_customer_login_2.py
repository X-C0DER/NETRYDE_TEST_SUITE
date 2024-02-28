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
    def test_e2e_customer_login(self, logged_in_browser):
        browser = logged_in_browser
        browser.find_element(By.CSS_SELECTOR, ".\\_nav-links_1xe3h_48 h1").click()
        time.sleep(2)
        assert browser.find_element(By.CSS_SELECTOR, ".\\_user-menu-logout-btn_1xe3h_219").text == "Logout"
    def test_booking():
        time.sleep(3)
        browser=logged_in_browser
        browser.find_element(By.CSS_SELECTOR, ".point-a").click()
        browser.find_element(By.CSS_SELECTOR, ".point-a").send_keys("2700 16th Avenue, Edgewood, Washington 98354, United States")
        browser.find_element(By.CSS_SELECTOR, ".point-a").send_keys(Keys.ENTER)
        browser.find_element(By.CSS_SELECTOR, ".point-b").click()

        browser.find_element(By.CSS_SELECTOR, ".point-b").send_keys("8407 Rainier Avenue South, Seattle, Washington 98118, United Statess")
        browser.find_element(By.CSS_SELECTOR, ".point-b").send_keys(Keys.ENTER)
        browser.find_element(By.ID, "time").click()
        
        current_date = datetime.now().date()
        next_day = (current_date + timedelta(days=1)).strftime("%m-%d-%Y")
        browser.find_element(By.ID, "time").send_keys(next_day)

        browser.find_element(By.XPATH, "(//input[@id=\'time\'])[2]").send_keys("16:02")
        browser.find_element(By.CSS_SELECTOR, "label:nth-child(2) > .icon").click()
        browser..find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/div[9]/button").click()
        
        assert True
    def test_stripe_payment():
        pass 

    def test_e2e_customer_logout(self, logged_in_browser):
        browser = logged_in_browser
        logout_btn=browser.find_element(By.CSS_SELECTOR, ".\\_user-menu-logout-btn_1xe3h_219")
        logout_btn.click()
        assert 'NetRyde' in browser.title


