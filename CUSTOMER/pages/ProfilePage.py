from .utils import * 

class ProfilePage:
	"""
    Class representing the profile page functionality.

    Attributes:
        driver: WebDriver object representing the browser instance.
        first_name: Locator for the first name input field.
        last_name: Locator for the last name input field.
        phone_no: Locator for the phone number input field.
        street: Locator for the street address input field.
        city: Locator for the city input field.
        state: Locator for the state input field.
        zip_code: Locator for the zip code input field.
    """
	def __init__(self,driver):
		"""
        Initializes the ProfilePage object with a WebDriver instance.

        Args:
            driver: WebDriver object representing the browser instance.
        """
		self.driver=driver
		self.first_name=(By.CSS_SELECTOR, ".driver-input-item:nth-child(2) > .driver-input-items:nth-child(1) > .userDataInputBox")
		self.last_name=(By.CSS_SELECTOR, ".driver-input-item:nth-child(2) > .driver-input-items:nth-child(2) > .userDataInputBox")
		self.phone_no=(By.CSS_SELECTOR, ".driver-input-items:nth-child(3) > .userDataInputBox")
		self.street= (By.CSS_SELECTOR, ".driver-input-item:nth-child(4) > .driver-input-items:nth-child(1) > .userDataInputBox")
		self.city=(By.CSS_SELECTOR, ".driver-input-item:nth-child(4) > .driver-input-items:nth-child(2) > .userDataInputBox")
		self.state=(By.CSS_SELECTOR, ".driver-input-item:nth-child(5) > .driver-input-items:nth-child(1) > .userDataInputBox")
		self.zip_code=(By.CSS_SELECTOR, ".driver-input-item:nth-child(5) > .driver-input-items:nth-child(2) > .userDataInputBox")
	
	def update_profile(self,fname,last_name,phone_no,street2,city,state,zip_code):
		"""
        Method to update user profile information.

        Args:
            fname: First name of the user.
            last_name: Last name of the user.
            phone_no: Phone number of the user.
            street2: Street address of the user.
            city: City of the user.
            state: State of the user.
            zip_code: Zip code of the user.
        """

		'''
		for locator in [self.first_name, self.last_name, self.phone_no, self.street, self.city, self.zip_code]:
		    input_field = self.driver.find_element(*locator)
		    input_field.clear()

		'''		
		self.driver.find_element(*self.first_name).clear()
		self.driver.find_element(*self.first_name).send_keys(fname)
		self.driver.find_element(*self.last_name).clear()
		self.driver.find_element(*self.last_name).send_keys(last_name)
		self.driver.find_element(*self.phone_no).clear()
		self.driver.find_element(*self.phone_no).send_keys(phone_no)
		self.driver.find_element(*self.street).clear()
		self.driver.find_element(*self.street).send_keys(street2)
		self.driver.find_element(*self.city).clear()
		self.driver.find_element(*self.city).send_keys(city)
		self.driver.find_element(*self.state).click()
		self.driver.find_element(By.XPATH, "//option[. = 'TX Texas']").click()
		self.driver.find_element(*self.zip_code).clear()
		self.driver.find_element(*self.zip_code).send_keys(zip_code)

		WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, "UpdateTextArea"))).click()
		