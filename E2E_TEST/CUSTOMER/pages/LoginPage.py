from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
	def __init__(self,driver):
		self.driver=driver
        self.email_input = (By.ID, "1")
        self.password_input = (By.ID, "3")
        self.logout_button = (By.CSS_SELECTOR, ".\\_user-menu-logout-btn_1xe3h_219")
		self.continue_button=driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
		self.form=driver.find_element(By.CSS_SELECTOR, ".auth-form").click()
		self.login_button=driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
