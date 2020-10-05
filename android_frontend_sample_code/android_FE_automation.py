# -*- coding: utf-8 -*-
import logging
import time
import unittest
import sys
import yaml

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class AndroidTestAutomation(unittest.TestCase):

    def setUp(self):
        self.android_desired_caps = {}
        self.android_desired_caps['platformName'] = 'Android'
        self.android_desired_caps['platformVersion'] = '10'
        self.android_desired_caps['deviceName'] = 'Galaxy Note S9'
        self.android_desired_caps['automationName'] = 'Appium'
        self.android_desired_caps['newCommandTimeout'] = 300
        self.android_desired_caps['appPackage'] = '{{apppackage_name}}'
        self.android_desired_caps['appActivity'] = '{{appactivity_name}}'
        self.android_desired_caps['noReset'] = True
        with open('../info.yaml') as ym:
            self.conf = yaml.load(ym, Loader=yaml.FullLoader)
        self.account_id = self.conf['account_email']
        self.password = self.conf['account_pass']
        self.name = self.conf['account_name']
        self.phone = self.conf['account_p_num']
        self.birth = self.conf['birth']

    def test_1_signin_signup(self):
        wd = webdriver.Remote('http://0.0.0.0:4724/wd/hub', self.android_desired_caps)
        time.sleep(2)
        wd.implicitly_wait(2)

        # test start
        try:
            wd.find_element_by_id('').click()
            wd.find_element_by_id('').text
            wd.find_element_by_id('').send_keys('')
            TouchAction(wd).press(x=100, y=100).move_to(x=300, y=300).release().perform()
            clipboard_text = wd.get_clipboard_text()
            time.sleep(1)
        except NoSuchElementException:
            logging.exception('error log')

        finally:
            wd.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTestAutomation)
    unittest.TextTestRunner(verbosity=2).run(suite)
