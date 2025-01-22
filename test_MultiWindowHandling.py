import time

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
import pytest
@pytest.fixture()
def environment_setup():
    global driver
    driver = Chrome()
    driver.get("https://thetestingworld.com/testings/")
    driver.maximize_window()
    yield
    driver.close()






def test_VerifyRegistration(environment_setup):

    driver.find_element(By.XPATH, "//label[text()='Login']").click()
    driver.find_element(By.NAME, "_txtUserName").send_keys("tester233")
    driver.find_element(By.NAME, "_txtPassword").send_keys("Tester233")
    driver.find_element(By.XPATH, "//input[@type='submit' and  @value='Login']").click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'My Account')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'Update')]").click()
    time.sleep(5)
    all_windows = driver.window_handles
    mainWin =""
    # print(all_windows)
    # for showing the print statement we have use  "- s"
    for win in all_windows:
        driver.switch_to.window(win)
        # print(driver.current_url)
        if driver.current_url == 'https://thetestingworld.com/testings/manage_customer.php':
            driver.find_element(By.XPATH, "//button[text()='Start Download']").click()
            time.sleep(5)
            driver.close()

        elif driver.current_url == 'https://thetestingworld.com/testings/dashboard.php':
            mainWin = win


    driver.switch_to.window(mainWin)
    print(driver.current_url)






