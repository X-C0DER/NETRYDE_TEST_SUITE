from .utils import * 

class HomePage:
	"""
    Class representing the functionality of the home page.

    Attributes:
        driver: WebDriver object representing the browser instance.
        pick_up_location: Locator for the pick-up location input field.
        drop_off_location: Locator for the drop-off location input field.
        get_price_button: Locator for the 'Get Price' button.
        book_trip_button: Locator for the 'Book Trip' button.
    """
	def __init__(self,driver):
		"""
        Initializes the HomePage object with a WebDriver instance.

        Args:
            driver: WebDriver object representing the browser instance.
        """
		self.driver=driver

		#Get Price 
		self.pick_up_location=(By.CSS_SELECTOR, ".point-a")
		self.drop_of_location=(By.CSS_SELECTOR, ".point-b")
		self.get_price_button=(By.ID, "Get PriceTextArea")
		self.book_trip_button=(By.TAG_NAME, "button")

	def get_price(self,point_a,point_b):
		"""
        Method to retrieve the price for a trip.

        Args:
            point_a: Pick-up location.
            point_b: Drop-off location.
        """
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".point-a"))).click()
		driver.find_element(By.CSS_SELECTOR, ".point-a").send_keys("2700 16th Avenue, Edgewood,")
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".suggestion:nth-child(1)"))).click()
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".point-b"))).click()
		driver.find_element(By.CSS_SELECTOR, ".point-b").send_keys("8407 Rainier Avenue South, Seattle,")
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".suggestion:nth-child(1)"))).click()
		driver.find_element(By.ID, "Get PriceTextArea").click()
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
		#WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".address--input-box > p"))

