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

class TestTCE2E002LOGIN2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCE2E002LOGIN2(self):
    self.driver.get("https://dev-np.netryde.com/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.ID, "Log inTextArea").click()
    self.driver.find_element(By.LINK_TEXT, "Login as a Customer").click()
    self.driver.find_element(By.ID, "1").send_keys("nrct1@zprodev.com")
    self.driver.find_element(By.ID, "3").send_keys("Test@123")
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".auth-form").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".point-a").click()
    self.driver.find_element(By.CSS_SELECTOR, ".point-a").send_keys("2700 16th Avenue, Edgewood, Washington 98354, United States")
    self.driver.find_element(By.CSS_SELECTOR, ".point-a").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").click()

    self.driver.find_element(By.CSS_SELECTOR, ".point-b").send_keys("8407 Rainier Avenue South, Seattle, Washington 98118, United Statess")
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "time").click()
    self.driver.find_element(By.ID, "time").send_keys("2024-02-28")
    self.driver.find_element(By.XPATH, "(//input[@id=\'time\'])[2]").click()
    self.driver.find_element(By.XPATH, "(//input[@id=\'time\'])[2]").send_keys("16:02")
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2) > .icon").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/div[9]/button").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".SubmitButton-IconContainer")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "cardNumber").click()
    self.driver.find_element(By.ID, "cardNumber").send_keys("4242 4242 4242 4242")
    self.driver.find_element(By.ID, "cardExpiry").send_keys("02 / 24")
    self.driver.find_element(By.ID, "billingName").send_keys("Michael Alem")
    self.driver.find_element(By.ID, "cardNumber").send_keys("4242 4242 4242 4242")
    self.driver.find_element(By.ID, "cardCvc").click()
    self.driver.find_element(By.ID, "cardCvc").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".SubmitButton-IconContainer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_booking-status-container_5f60k_426").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".\\_booking-status-container_5f60k_426").text == "Trip Booked\\\\nPayment Made\\\\nDriver Assigned"
    self.driver.find_element(By.LINK_TEXT, "Book another trip").click()
    self.driver.execute_script("window.scrollTo(0,0)")
  
