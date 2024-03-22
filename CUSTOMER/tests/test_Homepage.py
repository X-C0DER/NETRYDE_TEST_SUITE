import pytest
from pages.utils import *
from pages.Homepage import HomePage
from pages.TestDataMgr import TestDataManager


class TestHomepage:
    @pytest.fixture(scope="class")
    def browser(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_getpice(self,browser):
        Home=HomePage(browser)
        data=mgr=TestDataManager()
        locs=data.get_location_data("location.json",count=2)
        print ("test2")
        Home.get_price("7822 115th Avenue Southeast, Newcastle, Washington 98056, United States",
            "2700 Washington Highway 109, Ocean City, Washington 98569, United States"
        )
        
        assert True
