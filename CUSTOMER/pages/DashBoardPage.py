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
		self.comfortable_cars=(By.CSS_SELECTOR, "div:nth-child(3) > .car:nth-child(3) > label")
		self.book_tip_button=(By.XPATH, "//div[@id='root']/div/div/div[2]/div[9]/button")

	def multi_click(self,button_element, times):
	    for _ in range(times):
	        self.driver.find_element(By.CSS_SELECTOR,button_element).click()
	        time.sleep(0.5)



	def book_a_trip(self,
		point_a,point_b,pick_up_date,pick_up_time,
		passengers=1,flight_number=0,
		baby_on_board=0,car_seat=0,
		car="POPULAR",tip="NO_TIP",tip_amount=0
		):


		WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(1) > .car:nth-child(3) > label")))
		
		
	
		pick_up_loc = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.point_a))
		pick_up_loc.send_keys(point_a)
		pick_up_loc.send_keys(Keys.ENTER)
		#time.sleep(3)
		#self.driver.find_element(By.CSS_SELECTOR, ".suggestion:nth-child(1)").click()

		drop_off_loc = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.point_b))
		drop_off_loc.send_keys(point_b)
		#drop_off_loc.send_keys(Keys.ENTER)
		time.sleep(5)
		self.driver.find_element(By.CSS_SELECTOR, ".suggestion:nth-child(1)").click()
		
		
		
		if (car=="POPULAR"):
			self.driver.find_element(*self.popular_cars).click() 
		elif (car=="LUXURY"):
			self.driver.find_element(*self.luxury_cars).click()  
		elif (car=="COMFORTABLE"):
			self.driver.find_element(*self.comfortable_cars).click()


		if (passengers==1):
			pass
		else:
			self.multi_click("button:nth-child(4)",passengers-1)
			

		if (baby_on_board==0):
			pass
		else:
			self.driver.find_element(*self.popular_cars).click()
			self.driver.find_element(*self.baby_on_board).click()
			self.multi_click( ".\\_number-picker-container_5f60k_83:nth-child(6) > button:nth-child(4)",car_seat)


		if (flight_number==0):
			pass 
		else:
			self.driver.find_element(*self.flight_number).send_keys(flight_number)



		
		
		self.driver.find_element(*self.date_input).send_keys(pick_up_date)
		time.sleep(2)
		self.driver.find_element(*self.time_input).send_keys(pick_up_time)




		if (tip=="NO_TIP"):
			self.driver.find_element(*self.no_tip).click() 
		elif (tip=="TWENTY_FIVE"):
			self.driver.find_element(*self.tip_25).click()  
		elif (tip == "TWENTY"):
			self.driver.find_element(*self.tip_20).click()  
		elif (tip=="FIFTEEN"):
			self.driver.find_element(*self.tip_15).click()  
		elif (tip=="TEN"):
			self.driver.find_element(*self.tip_10).click()  
		elif (tip=="OTHER_AMOUNT"):
			self.driver.find_element(*self.tip_another_amount).click()
			self.multi_click(".\\_number-picker-container_5f60k_83:nth-child(3) > button:nth-child(4)",tip_amount)    



		
