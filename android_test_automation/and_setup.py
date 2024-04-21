from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions


def and_setup():
    android_caps = AppiumOptions()
    android_caps.set_capability('platformName', 'Android')
    android_caps.set_capability('platformVersion', '13')
    android_caps.set_capability('deviceName', 'Galaxy S22')
    android_caps.set_capability('automationName', 'UIAutomator2')
    android_caps.set_capability('newCommandTimeout', 300)
    android_caps.set_capability('appPackage', '{}')
    android_caps.set_capability('appActivity', '{}')
    android_caps.set_capability('noReset', True)
    android_caps.set_capability('appium:unlockType', 'pin')
    android_caps.set_capability('appium:unlockKey', '{}')
    android_caps.set_capability('udid', '{}')
    android_caps.set_capability('goog:chromeOptions', {'androidPackage': '{}', 'androidUseRunningApp': True,
                                                  'w3c': False})
    wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', options=android_caps)
    
    return wd, android_caps