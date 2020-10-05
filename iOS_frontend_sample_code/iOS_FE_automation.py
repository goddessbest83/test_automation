# -*- coding: utf-8 -*-
import logging
import time
import unittest
import HtmlTestRunner


from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, InvalidSessionIdException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class IOSTestAutomation(unittest.TestCase):

    def setUp(self):
        self.ios_desired_caps = {}
        self.ios_desired_caps['platformName'] = 'iOS'
        self.ios_desired_caps['platformVersion'] = '13.1'
        self.ios_desired_caps['deviceName'] = 'iPhone 7 Plus'
        self.ios_desired_caps['newCommandTimeout'] = 300
        self.ios_desired_caps['bundleId'] = '{{bundleid}}'
        self.ios_desired_caps['xcodeSigningId'] = 'iPhone Developer'
        self.ios_desired_caps['noReset'] = True
        self.ios_desired_caps['udid'] = '{{udid}}'
        self.ios_desired_caps['xcodeSigningId'] = 'iPhone Developer'
        with open('../info.yaml') as ym:
            self.conf = yaml.load(ym, Loader=yaml.FullLoader)
        self.account_id = self.conf['account_email']
        self.password = self.conf['account_pass']
        self.name = self.conf['account_name']
        self.phone = self.conf['account_p_num']
        self.birth = self.conf['birth']

    def test_1_signin_signup(self):
        wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', self.ios_desired_caps)
        time.sleep(2)
        wd.implicitly_wait(2)

        # test start
        try:
            wd.find_element_by_accessibility_id.click()
            wd.find_element_by_accessibility_id('').text
            wd.find_element_by_accessibility_id('').send_keys('')
            TouchAction(wd).press(x=100, y=100).move_to(x=300, y=300).release().perform()
            clipboard_text = wd.get_clipboard_text()
            time.sleep(1)
        except NoSuchElementException:
            logging.exception('error log')

        finally:
            wd.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IOSTestAutomation)
    HtmlTestRunner.HTMLTestRunner(output='suiteTest', report_title='iOS Automation Result').run(suite)