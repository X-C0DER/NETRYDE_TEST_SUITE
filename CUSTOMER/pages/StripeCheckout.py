from .utils import *

class StripeCheckout:
	def __init__(self,driver):
		self.driver=driver
		self.card_number=(By.ID, "cardNumber")
		self.card_expiry=(By.ID, "cardExpiry")
		self.card_cvc= (By.ID, "cardCvc")
		self.billng_name= (By.ID, "billingName")
		self.pay_btn=(By.CSS_SELECTOR, ".SubmitButton-IconContainer")
		self.trip_booked= (By.CSS_SELECTOR, ".\\_booking-status-item_5f60k_437:nth-child(1) > p")
		
	def pay_for_booking(self,card_number,card_expiry,card_cvc,billng_name):
		self.driver.find_element(*self.card_number).send_keys(card_number)
		self.driver.find_element(*self.card_expiry).send_keys(card_expiry)
		self.driver.find_element(*self.card_number).send_keys(card_cvc) 
		self.driver.find_element(*self.billng_name).send_keys(billng_name)
		self.driver.find_element(*self.pay_btn).click()

