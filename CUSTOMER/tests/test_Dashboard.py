import pytest
from pages.utils import *
from pages.DashBoardPage import DashBoard
from pages.LoginPage import LoginPage

class TestProfile:
    @pytest.fixture(scope="class")
    def browser(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()
        
    @pytest.fixture(scope="class")
    def logged_in_browser(self, browser):
        login_page = LoginPage(browser)
        login_page.login("nrct5@zprodev.com", "Test@123")
        yield browser
        '''
        (self,
        point_a,point_b,pick_up_date,pick_up_time,
        passengers=1,flight_number=0,
        baby_on_board=0,car_seat=0,
        car="POPULAR",tip="NO_TIP",tip_amount=0
        ):
        '''
    def date_and_time(self):
        current_date = datetime.now().date()
        next_day = (current_date + timedelta(days=1)).strftime("%m-%d-%Y")
        current_time = datetime.now()
        next_hour_time = current_time + timedelta(hours=6)
        six_hour = next_hour_time.strftime("%I:%M ")
        return next_day,six_hour

    def test_DashBoard(self,logged_in_browser):
        browser=logged_in_browser
        next_day,six_hour=self.date_and_time()
        dashboard=DashBoard(browser)
        dashboard.book_a_trip(point_a="2700 16th Avenue, Edgewood, ",
            point_b="9237 College Way North, Seattle,",
            pick_up_date=next_day,
            pick_up_time=six_hour,passengers=4,flight_number=22442,
            baby_on_board=2,car_seat=2,car="LUXURY",
            tip="TWENTY"
        )

        time.sleep(10)
        assert True
    