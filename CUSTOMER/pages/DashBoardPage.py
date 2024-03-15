from .utils import *

class DashBoard:
	def __init__(self,driver):
		self.driver=driver
		self.point_a=(By.CSS_SELECTOR, ".point-a")
		self.point_b=(By.CSS_SELECTOR, ".point-b")
		self.baby_on_board=(By.ID, "babyOnBoard")
		self.add_passenger_number=(By.CSS_SELECTOR, "button:nth-child(4)")
		self.decrease_passenger_number=(By.CSS_SELECTOR, "button:nth-child(2)")
		self.add_carseat=(By.CSS_SELECTOR, ".\\_number-picker-container_5f60k_83:nth-child(6) > button:nth-child(4)")
		self.decrease_carseat=(By.CSS_SELECTOR, ".\\_number-picker-container_5f60k_83:nth-child(6) > button:nth-child(2)")
		self.flight_number=(By.CSS_SELECTOR, ".\\_number-picker-container_5f60k_83:nth-child(1) > input")
		self.date_input=(By.ID, "time")
		self.time_input=(By.XPATH, "(//input[@id=\'time\'])[2]")
		self.tip_25=(By.CSS_SELECTOR, "label:nth-child(2) path")
		self.tip_20=(By.CSS_SELECTOR, "label:nth-child(4)")
		self.tip_15=(By.CSS_SELECTOR, "label:nth-child(6)")
		self.tip_10=(By.CSS_SELECTOR, "label:nth-child(8)")
		self.no_tip=(By.CSS_SELECTOR, "label:nth-child(10)")
		self.tip_another_amount=(By.CSS_SELECTOR, ".other-amount")
		self.add_tip=(By.CSS_SELECTOR, ".\\_number-picker-container_5f60k_83:nth-child(3) > button:nth-child(4)")
		self.decrease_tip=(By.CSS_SELECTOR, ".\\_number-picker-container_5f60k_83:nth-child(3) > button:nth-child(2)")
		self.popular_cars=(By.CSS_SELECTOR, "div:nth-child(1) > .car:nth-child(3) > label")
		self.luxury_cars=(By.CSS_SELECTOR, "div:nth-child(2) > .car:nth-child(3) > label")
		self.comfortabl_cars=(By.CSS_SELECTOR, "div:nth-child(3) > .car:nth-child(3) > label")
	def book_a_trip(self):
		self.driver.find_element(*self.point_a).click()
		
		pass
		
