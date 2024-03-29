import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging 

class TestTESTGETPRICE():
  def setup_method(self, method):
    logging.basicConfig(level=logging.INFO)
    options=Options()
    options.add_argument('--log-level=3')  
    options.add_argument("--headless")
    self.driver = webdriver.Chrome(options=options)
    
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC002GetPriceCustom(self):
    self.driver.get("https://dev-np.netryde.com/")
    self.driver.set_window_size(1218, 727)
    self.driver.find_element(By.CSS_SELECTOR, ".point-a").click()
    self.driver.find_element(By.CSS_SELECTOR, ".point-a").send_keys("Washington Heights,Washington, Georgia,United States")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".point-a").click()
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").send_keys("Washington Heights,Vermont, United States")
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".point-b").send_keys(Keys.ENTER)
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//button[@id='Get PriceTextArea']").click()
    time.sleep(5)
       
    wait = WebDriverWait(self.driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".address--input-box > p")))

    
    
    
    assert element.text == "Trip estimated to take 1106 Minutes"
