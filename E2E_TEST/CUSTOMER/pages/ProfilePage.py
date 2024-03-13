from .utils import * 

class ProfilePage:
	def __init__(self,driver):
		self.driver=driver
		self.first_name=(By.CSS_SELECTOR, ".driver-input-item:nth-child(2) > .driver-input-items:nth-child(1) > .userDataInputBox")
		self.last_name=(By.CSS_SELECTOR, ".driver-input-item:nth-child(2) > .driver-input-items:nth-child(2) > .userDataInputBox")
		self.phone_no=(By.CSS_SELECTOR, ".driver-input-item:nth-child(3) > .driver-input-items:nth-child(2) > .userDataInputBox")
		self.street= (By.CSS_SELECTOR, ".driver-input-item:nth-child(4) > .driver-input-items:nth-child(2) > .userDataInputBox")
		self.city=(By.CSS_SELECTOR, ".driver-input-item:nth-child(5) > .driver-input-items:nth-child(2) > .userDataInputBox") 
		self.state=(By.CSS_SELECTOR, ".driver-input-item:nth-child(6) > .driver-input-items:nth-child(2) > .userDataInputBox")
		self.zip_code= (By.CSS_SELECTOR, ".driver-input-item:nth-child(7) > .driver-input-items:nth-child(2) > .userDataInputBox")

	def update_profile(self,fname,last_name,phone_no,street,city,state,zip_code):
		pass
