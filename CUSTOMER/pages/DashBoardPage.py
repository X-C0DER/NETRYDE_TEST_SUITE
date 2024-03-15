from .utils import *

class DashBoard:
	def __init__(self,driver):
		self.driver=driver
		self.point_a=(By.CSS_SELECTOR, ".point-a")
		self.point_b=(By.CSS_SELECTOR, ".point-b")
		self.baby_on_board=(By.ID, "babyOnBoard")
		self.add_passenger_number=(By.CSS_SELECTOR, "button:nth-child(4)")
		self.decrease_passenger_number=(By.CSS_SELECTOR, "button:nth-child(2)")
		
		
