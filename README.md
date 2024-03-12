# NETRYDE TEST SUITE

This a Test Suite For Netryde Web Application.It Contains Happy and Negative Path Tests for the Three StakeHolders (Customer, Provider and admin). This Suite Is Designed Following the POM(Page Object Model) Architecture. 

Test Automatinon For NetRyde.com

Automation testing tool - Selenium WebDriver API
Programming language - Python
IDE - VsCode

prerequisites
python 3 and above
a virtual enviroment to run the python codes
selenium Webdriver

Geting Started 

1 clone a repository 
    git clone https://github.com/X-C0DER/NETRYDE_TEST_SUITE.git
2 navigate to a project directory
    cd NETRYDE_TEST_SUITE 
    cd E2E_TEST  /  MISC_TEST

Running Tests

1 run the tests using "pytest" command

    
```
NETRYDE_TEST_SUITE
│   README.md
│   location.json    
│   admin_data.json    
|   customer_data.json
|   provide_data.json
|
└───E2E_TEST
│   │   
│   │
│   └───CUSTOMER
│       │   test_LOGIN.py
│       │   utils.py
│       └───pages
│       │       Homepage.py
│       │       LoginPage.py
│       │       utils.py
│       └───tests
│       │       test_book.py
│       │       test_E2E_1.py
│       │       test_e2e_customer_login_1.py
│       │       test_e2e_customer_signup.py
│ 
└───MISC_TEST
    │   test_get_price.py
    │   test_recaptcha.py
    │   test_SHOW_PASSWORD.py
     
```