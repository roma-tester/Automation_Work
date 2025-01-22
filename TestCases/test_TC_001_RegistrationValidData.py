from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
from selenium.webdriver.common.by import By
import pytest
from DataGenerator import DataGen




@pytest.mark.parametrize('data', DataGen.dataGenerator())
def test_ValidRegistration(data):
    driver = InitiateDriver.startBrowser()
    # driver = Chrome()
    # driver.get("https://thetestingworld.com/testings/")
    # driver.maximize_window()
    # driver.find_element(By.NAME, "fld_username").send_keys("roma123")
    # driver.find_element(By.NAME, "fld_email").send_keys("romasingh123@gmail.com")
    # driver.find_element(By.NAME, ConfigReader.FetchElementLocator("Registration", "username_name")).send_keys("tester233")
    # driver.find_element(By.NAME, ConfigReader.FetchElementLocator("Registration", "user_email")).send_keys("tester233@gmail.com")
    # driver.close()
    register = RegistrationPage.RegistrationClass(driver)
    # register.enter_username("tester233")
    # register.enter_password("Tester233")
    # register.enter_email("tester233@gmail.com")
    register.enter_username(data[0])
    register.enter_password(data[1])