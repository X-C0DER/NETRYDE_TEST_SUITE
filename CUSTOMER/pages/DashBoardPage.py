from .utils import *
from DashBoardPage import DashBoard

class DashBoard:
	"""
    Class representing the dashboard functionality for booking a trip.

    Attributes:
        driver: WebDriver object representing the browser instance.
        point_a: Locator for the pick-up location input field.
        point_b: Locator for the drop-off location input field.
        baby_on_board: Locator for the 'Baby On Board' checkbox.
        add_passenger_number: Locator for the 'Add Passenger' button.
        decrease_passenger_number: Locator for the 'Decrease Passenger' button.
        add_carseat: Locator for the 'Add Car Seat' button.
        decrease_carseat: Locator for the 'Decrease Car Seat' button.
        flight_number: Locator for the flight number input field.
        date_input: Locator for the pick-up date input field.
        time_input: Locator for the pick-up time input field.
        tip_25: Locator for the 25% tip option.
        tip_20: Locator for the 20% tip option.
        tip_15: Locator for the 15% tip option.
        tip_10: Locator for the 10% tip option.
        no_tip: Locator for the 'No Tip' option.
        tip_another_amount: Locator for the 'Other Amount' tip option.
        add_tip: Locator forgit  the 'Add Tip' button.
        decrease_tip: Locator for the 'Decrease Tip' button.
        popular_cars: Locator for the 'Popular Cars' option.
        luxury_cars: Locator for the 'Luxury Cars' option.
        comfortable_cars: Locator for the 'Comfortable Cars' option.
        book_tip_button: Locator for the 'Book Trip' button.
    """
	def __init__(self,driver):

		"""
        Initializes the Dashboard object with a WebDriver instance.

        Args:
            driver: WebDriver object representing the browser instance.
        """
		self.driver=driver

		# Define locators for various elements on the dashboard
		self.point_a=(By.CSS_SELECTOR, ".point-a")
		self.point_b=(By.CSS_SELECTOR, ".point-b")
		self.baby_on_board=(By.ID, "babyOnBoard")
		self.add_passenger_number=(By.CSS_SELECTOR, "button:nth-child(4)")
		self.decrease_passenger_number=(By.CSS_SELECTOR, "button:nth-child(2)")
		self.passengers=(By.CSS_SELECTOR, ".\\_number-picker-container_5f60k_83:nth-child(4) > input")
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
		self.map_canvas=(By.CSS_SELECTOR,".mapboxgl-canvas")
		self.clear_point_b=(By.CSS_SELECTOR,".close--btn-b")
		self.clear_point_a=(By.CSS_SELECTOR,".close--btn-a > path")

	def multi_click(self,button_element, times):
		"""
        Method to perform multiple clicks on a specified button.

        Args:
            button_element: Locator for the button element.
            times: Number of times to click the button.
        """
		for _ in range(times):
			self.driver.find_element(By.CSS_SELECTOR,button_element).click()
			time.sleep(0.5)


	def choose_location(self,point):
		suggestion_elements = WebDriverWait(self.driver, 20).until(
		EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.suggestion'))
		)

		for suggestion in suggestion_elements:
			suggestion_text = suggestion.text
			if point in suggestion_text:
				suggestion.click()
				break 

	def book_a_trip(
			self,
			point_a,point_b,pick_up_date,pick_up_time,
			passengers=1,flight_number=0,
			baby_on_board=0,car_seat=0,
			car="POPULAR",tip="NO_TIP",tip_amount=0
			):
			"""
			Method to book a trip with various options.g9
			Args:
				point_a: Pick-up location.
				point_b: Drop-off location.
				pick_up_date: Date for pick-up.
				pick_up_time: Time for pick-up.
				passengers: Number of passengers (default is 1).
				flight_number: Flight number (default is 0).
				baby_on_board: Whether baby is on board (default is 0).
				car_seat: Number of car seats required (default is 0).
				car: Type of car (default is "POPULAR").
				tip: Type of tip (default is "NO_TIP").
				tip_amount: Amount of tip (default is 0).
			"""
			
			

			# Wait for the attribute of the map container element to have the expected value
			#WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(())).click()
			


			#WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(*self.point_a))
			self.driver.find_element(*self.point_a).send_keys(point_a)
			time.sleep(3)
			self.choose_location(point_a)
			time.sleep(3)
			self.driver.find_element(*self.point_a).click()

			self.driver.find_element(*self.point_b).click()
			self.driver.find_element(*self.point_b).send_keys(point_b)
			time.sleep(5)
			self.choose_location(point_b)
			time.sleep(2)
			self.driver.find_element(*self.point_b).click()

			

			
			if (car=="POPULAR"):
				self.driver.find_element(*self.popular_cars).click() 
			elif (car=="LUXURY"):
				self.driver.find_element(*self.luxury_cars).click()  
			elif (car=="COMFORTABLE"):
				self.driver.find_element(*self.comfortable_cars).click()


			if (passengers==1):
				pass
			else:
				self.driver.find_element(*self.passengers).clear()
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
				self.driver.find_element(*self.flight_number).clear()
				self.driver.find_element(*self.flight_number).send_keys(flight_number)



			
			
			self.driver.find_element(*self.date_input).clear()
			self.driver.find_element(*self.date_input).send_keys(pick_up_date)
			
			self.driver.find_element(*self.time_input).clear()
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


			time.sleep(5)
		



		
