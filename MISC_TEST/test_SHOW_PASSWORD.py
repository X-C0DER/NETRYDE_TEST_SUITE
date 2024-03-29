import pytest
import time
import json
from logging import info,debug
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTCMISCSHOWPASSWORD():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCMISCSHOWPASSWORD(self):
    self.driver.get("https://dev-np.netryde.com/")
    self.driver.set_window_size(1218, 727)
    self.driver.find_element(By.ID, "Sign upTextArea").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_user-menu-link_1tnn4_70:nth-child(1) path").click()
    self.driver.find_element(By.ID, "1").send_keys("salazaralem@gmail.com")
    info ("Entering Email: salazaralem@gmail")
    self.driver.find_element(By.ID, "3").send_keys("M!k3th3fr34k")
    info("Enterinng Password")
    self.driver.find_element(By.CSS_SELECTOR, ".auth-page").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()

    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    time.sleep(2)
    print ("Checking if Checkbox is Checked")
    assert self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").is_selected() is True

