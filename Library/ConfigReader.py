
# create and read data from config files
import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    # config.read("../ConfigFiles/Config.cfg")
    config.read("./ConfigFiles/Config.cfg")
    return config.get(section, key)



# print(readConfigData('Details', 'Application_URL'))

def FetchElementLocator(section, key):
    config = configparser.ConfigParser()
    # config.read("../ConfigFiles/Config.cfg")
    config.read("./ConfigFiles/Elements.cfg")
    return config.get(section, key)
