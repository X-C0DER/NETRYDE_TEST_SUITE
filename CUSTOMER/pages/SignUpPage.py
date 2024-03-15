from .utils import *

class SignUpPage:
	def __init__(self,driver):
		self.driver=driver

		self.signup_nav=(By.ID, "Sign upTextArea")
		self.accept_terms=(By.ID, "AcceptTextArea")
		self.signup_link=(By.LINK_TEXT, "Sign Up to book")

		self.email=(By.ID, "1")
		self.password_1=(By.ID, "3")
		self.password_2=(By.ID, "4")

		self.cont_b_1=(By.CSS_SELECTOR, "button:nth-child(3)")
		self.cont_b_2=(By.CSS_SELECTOR, "button:nth-child(4)")

		#self.verification=(By.CSS_SELECTOR, "h2")

	def SignUp(self,email,password):
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email)).send_keys(email)

		self.driver.find_element(*self.password_1).send_keys(password)
		self.driver.find_element(*self.cont_b_1).click()

		self.driver.find_element(*self.password_2).send_keys(password)
		self.driver.find_element(*self.cont_b_2).click()
		self.driver.find_element(*self.cont_b_2).click()
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.accept_terms)).click()
		
		time.sleep(3)

		self.driver.find_element(*self.cont_b_2).click()


		


