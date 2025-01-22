from selenium.webdriver.common.by import By

from Library import ConfigReader

class RegistrationClass:


    def __init__(self, obj):
        global driver
        driver = obj


    def enter_username(self, username):
        driver.find_element(By.NAME, ConfigReader.FetchElementLocator("Registration", "username_name")).send_keys(
            username)


    def enter_password(self, password):
        driver.find_element(By.NAME, ConfigReader.FetchElementLocator("Registration", "user_pass")).send_keys(
            password)


    def enter_email(self, email):
        driver.find_element(By.NAME, ConfigReader.FetchElementLocator("Registration", "user_email")).send_keys(
            email)



