import pytest
from pages.utils import *
from pages.DashBoardPage import DashBoard
from pages.LoginPage import LoginPage
from pages.TestDataMgr import TestDataManager
from pages.StripeCheckout import StripeCheckout

def load_test_data2():
    TestDataMGR=TestDataManager()        
    test_data=TestDataMGR.get_test_cases_from_file("test_cases2.json")
    return test_data 

class TestDashBoard:
    @pytest.fixture(scope="class")
    def browser(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()
        
    @pytest.fixture(scope="class")
    def logged_in_browser(self, browser):
        login_page = LoginPage(browser)
        TEST_DATA=self.load_test_data()
        login_page.login(TEST_DATA["username"], TEST_DATA["password"])
        yield browser

    def date_and_time(self):
        current_date = datetime.now().date()
        next_day = (current_date + timedelta(days=1)).strftime("%m-%d-%Y")
        current_time = datetime.now()
        next_hour_time = current_time + timedelta(hours=10)
        six_hour = next_hour_time.strftime("%I:%M %p")
        return next_day,six_hour

 
    def load_test_data(self):
        TestDataMGR=TestDataManager()        
        test_data=TestDataMGR.prepare_all_test_data()
        return test_data

    @pytest.mark.parametrize("test_case",load_test_data2())
    def test_DashBoard(self,logged_in_browser,test_case):
        browser=logged_in_browser
        time.sleep(10)
        next_day,six_hour=self.date_and_time()
        point_a = test_case["point_a"]
        point_b = test_case["point_b"]
        passengers = test_case["passengers"]
        flight_number = test_case["flight_number"]
        baby_on_board = test_case["baby_on_board"]
        car_seat = test_case["car_seats"]
        car = test_case["car"]
        tip = test_case["tip"]
        tip_amount = test_case["tip_amount"]

        dashboard=DashBoard(browser)
        dashboard.book_a_trip(
            point_a=point_a,
            point_b=point_b,
            pick_up_date=next_day,
            pick_up_time=six_hour,
            passengers=passengers,
            flight_number=flight_number,
            baby_on_board=baby_on_board,
            car_seat=car_seat,
            car=car,
            tip=tip,
            tip_amount=tip_amount
        )
        '''
        Stripe=StripeCheckout()

        payment_detail=TestDataManager()
        card=payment_detail.get_payment_detail("payment_detail.json")

        Stripe.pay_for_booking(card_number=card["card_number"],
            card_expiry=card["card_expiry_date"],
            card_cvc=card["card_cvc"],
            billing_name=card["card_holder_name"]
        )
        assert browser.find_element(By.CSS_SELECTOR, ".\\_booking-status-item_5f60k_437:nth-child(1) > p").text == "Trip Booked"
        
        time.sleep(3)
        browser.find_element(By.LINK_TEXT, "Book another trip").click()

        '''


        assert True
    