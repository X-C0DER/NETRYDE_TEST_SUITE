import pytest
import time
from datetime import datetime,timedelta
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def logged_in_browser(browser):
    browser.get("https://dev-np.netryde.com/")
    browser.maximize_window()
    browser.find_element(By.ID, "Log inTextArea").click()
    browser.find_element(By.LINK_TEXT, "Login as a Customer").click()
    browser.find_element(By.ID, "1").send_keys("nrct1@zprodev.com")
    browser.find_element(By.ID, "3").send_keys("Test@123")
    browser.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
    browser.find_element(By.CSS_SELECTOR, ".auth-form").click()
    browser.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    time.sleep(5)
    yield browser

class TestE2ECustomerLogin:
    def test_e2e_customer_login(self, logged_in_browser):
        time.sleep(3)
        browser = logged_in_browser 
        assert 'https://dev-np.netryde.com/dashboard/map' in browser.current_url

    def test_e2e_get_price(self,logged_in_browser):
        browser=logged_in_browser
        browser.get("https://dev-np.netryde.com/")
        browser.find_element(By.CSS_SELECTOR, ".point-a").click()
        browser.find_element(By.CSS_SELECTOR, ".point-a").send_keys("2700 16th Avenue, Edgewood,")
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, ".suggestion:nth-child(1)").click()

        browser.find_element(By.CSS_SELECTOR, ".point-b").click()
        browser.find_element(By.CSS_SELECTOR, ".point-b").send_keys("8407 Rainier Avenue South, Seattle,")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, ".suggestion:nth-child(1)").click()
        time.sleep(2)
        browser.find_element(By.ID, "Get PriceTextArea").click()
        time.sleep(3)
        element = browser.find_element(By.TAG_NAME, "button")
        element.click()
        time.sleep(3)

        assert 'https://dev-np.netryde.com/dashboard/map' in browser.current_url


    def test_booking(self,logged_in_browser):
        
        browser=logged_in_browser

        # browser.find_element(By.CSS_SELECTOR, ".point-a").click()
        # browser.find_element(By.CSS_SELECTOR, ".point-a").clear()
        # browser.find_element(By.CSS_SELECTOR, ".point-a").send_keys("8407 Rainier Avenue South, Seattle, Washington 98118, United States")
        # time.sleep(3)
        # browser.find_element(By.CSS_SELECTOR, ".suggestion:nth-child(1)").click()
        # #browser.find_element(By.CSS_SELECTOR, ".point-a").send_keys(Keys.ENTER)

        
        # browser.find_element(By.CSS_SELECTOR, ".point-b").click()
        # browser.find_element(By.CSS_SELECTOR, ".point-b").send_keys("2700 16th Avenue, Edgewood, Washington 98354, United States")
        # time.sleep(5)
        # browser.find_element(By.CSS_SELECTOR, ".suggestion:nth-child(1)").click() 



        current_date = datetime.now().date()
        next_day = (current_date + timedelta(days=1)).strftime("%m-%d-%Y")
        current_time = datetime.now()
        next_hour_time = current_time + timedelta(hours=6)
        six_hour = next_hour_time.strftime("%H-%M")
        date_input=browser.find_element(By.XPATH, "//div[@id='root']/div/div/div[2]/div[9]/div/input")
        time_input=browser.find_element(By.XPATH, "(//input[@id=\'time\'])[2]")

       
        date_input.send_keys(next_day)
        time.sleep(2)
        time_input.send_keys(six_hour)

        time.sleep(3)

        browser.find_element(By.CSS_SELECTOR, "label:nth-child(10)").click()
        browser.find_element(By.XPATH, "//div[@id='root']/div/div/div[2]/div[9]/button").click()
        
        
        time.sleep(5)
        assert 'https://checkout.stripe.com' in browser.current_url

    def test_stripe_checkout(self,logged_in_browser):
        browser=logged_in_browser
        browser.find_element(By.ID, "cardNumber").click()
        
        
        browser.find_element(By.ID, "cardNumber").send_keys("4242 4242 4242 4242")
        
        browser.find_element(By.ID, "cardExpiry").send_keys("04 / 24")
        
        browser.find_element(By.ID, "cardCvc").send_keys("123")

        browser.find_element(By.ID, "billingName").send_keys("Michael Alem")
        
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, ".SubmitButton-IconContainer").click()
        time.sleep(8)
        browser.find_element(By.CSS_SELECTOR, ".\\_booking-status-container_5f60k_426").click()
        time.sleep(5)
        assert browser.find_element(By.CSS_SELECTOR, ".\\_booking-status-item_5f60k_437:nth-child(1) > p").text == "Trip Booked"
        browser.execute_script("window.scrollTo(0, 250);")
        time.sleep(3)
        browser.find_element(By.LINK_TEXT, "Book another trip").click()

    def test_booking2(self,logged_in_browser):
        pass


    def test_e2e_customer_logout(self, logged_in_browser):
        browser = logged_in_browser
        browser.execute_script("window.scrollTo(0, -100);")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, ".\\_nav-links_1xe3h_48 h1").click()
        time.sleep(3)
        logout_btn=browser.find_element(By.CSS_SELECTOR, ".\\_user-menu-logout-btn_1xe3h_219")
        logout_btn.click()
        time.sleep(3)
        assert 'NetRyde' in browser.title



