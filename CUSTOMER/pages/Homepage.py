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
		self.driver.get("https://dev-np.netryde.com")
		self.driver.maximize_window()
		
    
		
		self.driver.find_element(By.CSS_SELECTOR, ".point-a").click()
		self.driver.find_element(By.CSS_SELECTOR, ".point-a").send_keys(point_a)
		time.sleep(2)
		self.driver.find_element(By.CSS_SELECTOR, ".suggestion:nth-child(1)").click()

		self.driver.find_element(By.CSS_SELECTOR, ".point-b").click()
		self.driver.find_element(By.CSS_SELECTOR, ".point-b").send_keys(point_b)
		time.sleep(5)
		self.driver.find_element(By.CSS_SELECTOR, ".suggestion:nth-child(1)").click()
		time.sleep(2)
		self.driver.find_element(By.ID, "Get PriceTextArea").click()
		time.sleep(3)
		element = self.driver.find_element(By.XPATH, "//div[@id='root']/div/div/div/div/div/div[2]/div/div/div/div[2]/button")
		element.click()
		time.sleep(3)


