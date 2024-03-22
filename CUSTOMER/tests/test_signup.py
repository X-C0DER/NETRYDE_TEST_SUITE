import pytest
from pages.utils import *
from pages.SignUpPage import SignUpPage
from .pages.TestDataMgr import TestDataManager


class TestSignup():  

  @pytest.fixture(scope="class")
  def browser(self):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

  def test_signup(self,browser):
    sign_up=SignUpPage(browser)

    browser.get("https://dev-np.netryde.com/")
    browser.find_element(By.ID, "Sign upTextArea").click()
    browser.find_element(By.CSS_SELECTOR, ".\\_user-menu-link_huwg0_70:nth-child(1) > svg").click()
    user=TestDataManager()
    test_user=user.get_user_data()
    sign_up.SignUp(test_user["username"],test_user["password"])
    WebDriverWait(browser, 10).until(EC.url_to_be("https://dev-np.netryde.com/registrationSuccess"))
    
    assert 'https://dev-np.netryde.com/registrationSuccess' in browser.current_url
  
