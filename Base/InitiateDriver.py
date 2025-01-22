from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from Library import ConfigReader


def startBrowser():
    global driver

    if ConfigReader.readConfigData('Details', 'Browser') == 'Chrome' :
        driver = Chrome()

    elif ConfigReader.readConfigData('Details', 'Browser') == 'Firefox' :
        driver = Firefox()

    else:
        driver = Edge()

    # driver.get("https://thetestingworld.com/testings/")
    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver


def closeBrowser():
    driver.close()