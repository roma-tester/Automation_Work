from selenium.webdriver.common.by import By

from Base import InitiateDriver
from Library import ConfigReader

def test_InvalidDataRegistration():

    driver = InitiateDriver.startBrowser()
    # driver.find_element(By.NAME, "fld_password").send_keys("roma1234")
    # driver.find_element(By.NAME, ConfigReader.FetchElementLocator("Registration", "user_pass")).send_keys("roma1234")