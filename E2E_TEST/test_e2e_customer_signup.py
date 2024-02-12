import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestSignUpProcess():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_sign_up_process(self):
        self.driver.get("https://dev-np.netryde.com/")
        self.driver.set_window_size(1218, 727)
        

        self.driver.find_element(By.ID, "Sign upTextArea").click()


        self.driver.find_element(By.CSS_SELECTOR, ".\\_user-menu-link_1tnn4_70:nth-child(1) > svg").click()
   
        email_input = self.driver.find_element(By.ID, "1")
        email_input.send_keys("bibgxjhj@gmail.com")

    
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()


        self.driver.execute_script("window.scrollTo(0,0)")


        password_input = self.driver.find_element(By.ID, "3")
        password_input.send_keys("M!k3th3fr34k")

 
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()

 
        confirm_password_input = self.driver.find_element(By.ID, "4")
        confirm_password_input.send_keys("M!k3th3fr34k")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
        time.sleep(3)
      
        accept_button = WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div/div[2]/button[2]"))
        )
        accept_button.click()
       
        self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/div[2]/div[2]/button").click()
        time.sleep(5)
    
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "A verification link has been sent to your email"


