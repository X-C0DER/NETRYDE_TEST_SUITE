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

class TestTCE2E002LOGIN1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCE2E002LOGIN1(self):
    self.driver.get("https://dev-np.netryde.com/")
    self.driver.set_window_size(1218, 727)
    self.driver.find_element(By.CSS_SELECTOR, ".point-a").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".point-a").send_keys("Washington Heights,Washington, Georgia,United States")
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").click()
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").click()
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").click()
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").send_keys(" Washington Heights,Vermont, United States")
    
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").click()
    self.driver.find_element(By.XPATH, "//button[@id='Get PriceTextArea']").click()
    time.sleep(3)
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div/div/div/div[2]/div/div/div/div[2]/button").click()
    time.sleep(5) 
    self.driver.find_element(By.ID, "1").click()
    self.driver.find_element(By.ID, "1").send_keys("nrct1@zprodev.com")
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "3").click()
    self.driver.find_element(By.ID, "3").click()
    self.driver.find_element(By.ID, "3").send_keys("M!k3th3fr34k")
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    time.sleep(10)
    assert self.driver.title == "NetRyde"
  
