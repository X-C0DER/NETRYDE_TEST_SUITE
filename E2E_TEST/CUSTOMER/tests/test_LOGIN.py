import pytest
from pages.utils import *
from pages.LoginPage import LoginPage

class TestLogin:
    @pytest.fixture(scope="class")
    def browser(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_login(self, browser):
        login_page = LoginPage(browser)
        login_page.login("nrct1@zprodev.com", "Test@123")
        WebDriverWait(browser, 10).until(EC.url_to_be("https://dev-np.netryde.com/dashboard/map"))
        assert 'https://dev-np.netryde.com/dashboard/map' in browser.current_url

