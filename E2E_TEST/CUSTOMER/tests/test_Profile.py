import pytest
from pages.utils import *
from pages.ProfilePage import ProfilePage
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
        login_page.login("nrct2@zprodev.com", "Test@123")
        yield browser
    
    def test_UpdateProfile(self, logged_in_browser):
        browser = logged_in_browser
        time.sleep(3)

        browser.get("https://dev-np.netryde.com/dashboard/user-profile")

        
        #browser.find_element(By.CSS_SELECTOR, ".auth-page").click()
        time.sleep(3)
        profile = ProfilePage(browser)
        profile.update_profile("Michael", "Alem", "251923443422", "Evergreen Terrace", "Seattle", "Washington", "98101")
        

        btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "Continue to bookTextArea")))
        assert 'Continue to book' in btn.text

