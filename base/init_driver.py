from appium import webdriver


def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    # desired_caps['noReset'] = 'true'
    # app的信息
    desired_caps['appPackage'] = 'xxx'
    desired_caps['appActivity'] = 'xxx'
    # 支持输入中文
    desired_caps['uncodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明 driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
