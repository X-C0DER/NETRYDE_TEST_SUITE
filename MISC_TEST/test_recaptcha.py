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

class TestTC2001TESTCAPTCHA():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC2001TESTCAPTCHA(self):
    self.driver.get("https://dev-np.netryde.com/")
    self.driver.set_window_size(1218, 727)
    self.driver.find_element(By.ID, "Log inTextArea").click()
    self.driver.find_element(By.LINK_TEXT, "Login as a Customer").click()
    self.driver.find_element(By.ID, "1").send_keys("salazaralem@gmail.com")
    self.driver.find_element(By.ID, "3").send_keys("M!k3th3fr34k")
    self.driver.find_element(By.ID, "1").click()
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "3").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    time.sleep(3)
    assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(3)").text == "captcha verification process failed"

  
