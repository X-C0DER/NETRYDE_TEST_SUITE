from .utils import * 

class HomePage:
	def __init__(self,driver):
		self.driver=driver

		#Get Price 
		self.pick_up_location=(By.CSS_SELECTOR, ".point-a")
		self.drop_of_location=(By.CSS_SELECTOR, ".point-b")
		self.get_price_button=(By.ID, "Get PriceTextArea")
		self.book_trip_button=(By.TAG_NAME, "button")

	def get_price(self,point_a,point_b):
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".point-a"))).click()
		driver.find_element(By.CSS_SELECTOR, ".point-a").send_keys("2700 16th Avenue, Edgewood,")
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".suggestion:nth-child(1)"))).click()
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".point-b"))).click()
		driver.find_element(By.CSS_SELECTOR, ".point-b").send_keys("8407 Rainier Avenue South, Seattle,")
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".suggestion:nth-child(1)"))).click()
		driver.find_element(By.ID, "Get PriceTextArea").click()
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
		#WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".address--input-box > p"))

