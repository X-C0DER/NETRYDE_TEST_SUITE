from .utils import *

class SignUpPage:
	"""
    Class representing the sign-up page functionality.

    Attributes:
        driver: WebDriver object representing the browser instance.
        signup_nav: Locator for the sign-up navigation element.
        accept_terms: Locator for the 'Accept' terms checkbox.
        signup_link: Locator for the sign-up link.
        email: Locator for the email input field.
        password_1: Locator for the first password input field.
        password_2: Locator for the second password input field.
        cont_b_1: Locator for the 'Continue' button 1.
        cont_b_2: Locator for the 'Continue' button 2.
    """
	def __init__(self,driver):
		"""
        Initializes the SignUpPage object with a WebDriver instance.

        Args:
            driver: WebDriver object representing the browser instance.
        """
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
		"""
        Method to perform sign-up.

        Args:
            email: Email address of the user.
            password: Password of the user.
        """
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email)).send_keys(email)

		self.driver.find_element(*self.password_1).send_keys(password)
		self.driver.find_element(*self.cont_b_1).click()

		self.driver.find_element(*self.password_2).send_keys(password)
		self.driver.find_element(*self.cont_b_2).click()
		self.driver.find_element(*self.cont_b_2).click()
		WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.accept_terms)).click()
		
		time.sleep(3)

		self.driver.find_element(*self.cont_b_2).click()


		


