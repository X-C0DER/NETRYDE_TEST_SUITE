from pages.utils import *
from pages.SignUpPage import SignUpPage

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

    sign_up.SignUp("nrct1@zprodev.com","Test@123")
    verification= WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))

    time.sleep(10)
    assert verification.text == "A verification link has been sent to your email"
  
