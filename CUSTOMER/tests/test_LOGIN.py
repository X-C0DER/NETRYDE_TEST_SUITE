import pytest
from pages.utils import *
from pages.LoginPage import LoginPage
from .TestDataMgr import TestDataManager


class TestLogin:
    @pytest.fixture(scope="class")
    def browser(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_login(self, browser):
        login_page = LoginPage(browser)
        user=TestDataManager()
        email_password=user.get_user_data("customer_data.json")
        login_page.login(email_password["username"], email_password["password"])
        WebDriverWait(browser, 10).until(EC.url_to_be("https://dev-np.netryde.com/dashboard/map"))
        assert 'https://dev-np.netryde.com/dashboard/map' in browser.current_url

