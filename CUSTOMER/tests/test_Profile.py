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
        login_page.login("nrct5@zprodev.com", "Test@123")
        yield browser
    
    def test_UpdateProfile(self, logged_in_browser):
        browser = logged_in_browser
        
       
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h1"))).click()
        browser.find_element(By.LINK_TEXT, "Profile").click()

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "UpdateTextArea")))
        
  
        profile = ProfilePage(browser)
        profile.update_profile("Michael", "Alem", "251923443422", "Evergreen Terrace", "Seattle", "Washington", "98101")
        

        btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "Continue to bookTextArea")))
       
        assert 'Continue to book' in btn.text

