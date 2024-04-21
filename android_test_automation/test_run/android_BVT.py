import unittest
import json

from appium.webdriver.appium_service import AppiumService
from selenium.common.exceptions import InvalidSessionIdException
from android_test_automation import and_setup
from android_test_automation.test_cases.android_test import AutomationTesting


class AndroidTestAutomation(unittest.TestCase):

    def setUp(self):

        # Appium Service
        self.appium = AppiumService()
        self.appium.start(args=['-p', '4723', '--base-path', '/wd/hub', '--default-capabilities', '{"appium:chromedriverExecutable": "/usr/local/bin/chromedriver"}'])

        # webdriver
        self.wd, self.and_cap = and_setup.and_setup()
        self.wd.implicitly_wait(5)

    def tearDown(self):
        try:
            self.wd.quit()
            self.appium.stop()
        except InvalidSessionIdException:
            self.appium.stop()

    def test_sample(self):
        error_text = AutomationTesting.default_test(self, self.wd)


if __name__ == '__main__':
    unittest.main()
