import pytest
from pages.utils import *
from pages.Homepage import HomePage
from .TestDataMgr import TestDataManager


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

        Home.get_price(locs[0],locs[1])
        time.sleep(10)
        assert True
