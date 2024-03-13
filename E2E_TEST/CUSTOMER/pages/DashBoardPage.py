from .utils import *

class DashBoard:
	def __init__(self,driver):
		self.driver=driver
		self.point_a=(By.CSS_SELECTOR, ".point-a")
		self.point_b=(By.CSS_SELECTOR, ".point-b")
		
