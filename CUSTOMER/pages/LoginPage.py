from .utils import *

class LoginPage:
	def __init__(self,driver):
		
		self.driver=driver
		self.email_input = (By.ID, "1")
		self.password_input = (By.ID, "3")
		self.continue_button=(By.CSS_SELECTOR, "button:nth-child(3)")
		self.form=(By.CSS_SELECTOR, ".auth-form")
		self.login_button=(By.CSS_SELECTOR, "button:nth-child(4)")

	def login(self, email, password):
		self.driver.get("https://dev-np.netryde.com/")
		self.driver.maximize_window()
		self.driver.find_element(By.ID, "Log inTextArea").click()
		self.driver.find_element(By.LINK_TEXT, "Login as a Customer").click()
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email_input)).send_keys(email)
		self.driver.find_element(*self.continue_button).click()
		self.driver.find_element(*self.password_input).send_keys(password)
		self.driver.find_element(*self.form).click()
		self.driver.find_element(*self.login_button).click()
