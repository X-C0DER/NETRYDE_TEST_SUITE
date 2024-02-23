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


class Test_E2E_CUSTOMEER_LOGIN2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  '''def teardown_method(self, method):
    self.driver.quit()
  '''
  def test_e2e_customer_login_2(self):
    self.driver.get("https://dev-np.netryde.com/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.ID, "Log inTextArea").click()
    self.driver.find_element(By.LINK_TEXT, "Login as a Customer").click()
    self.driver.find_element(By.ID, "1").send_keys("nrct2@zprodev.com")
    self.driver.find_element(By.ID, "3").send_keys("Test@123")
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()

    self.driver.find_element(By.CSS_SELECTOR, ".auth-form").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".\\_nav-links_1xe3h_48 h1").click()

    time.sleep(2)
    assert self.driver.find_element(By.CSS_SELECTOR, ".\\_user-menu-logout-btn_1xe3h_219").text == "Logout"
    

  

