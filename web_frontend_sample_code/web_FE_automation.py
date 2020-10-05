import datetime
import json
import logging
import time
import requests
import unittest
import urllib3
import yaml

from nose.tools import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class WebTestAutomation(unittest.TestCase):

    def setUp(self):
        # mac
        self.wd = webdriver.Chrome('/usr/local/bin/chromedriver')
        with open('../info.yaml') as ym:
            self.conf = yaml.load(ym, Loader=yaml.FullLoader)
        self.account_id = self.conf['account_email']
        self.password = self.conf['account_pass']
        self.name = self.conf['account_name']
        self.phone = self.conf['account_p_num']
        self.birth = self.conf['birth']

    def test_1_selenium_start(self):
        try:
            wd = self.wd
            wd.maximize_window()
            wait = WebDriverWait(wd, 10)

            wd.get(self.s_address)
            wd.refresh()

            ActionChains(wd).key_down(Keys.ENTER).perform()
            ActionChains(wd).key_down(Keys.TAB).perform()
            ActionChains(wd).key_down(Keys.ARROW_DOWN).perform()
            ActionChains(wd).send_keys(Keys.ESCAPE).perform()

            wd.find_element_by_id('').send_keys('')
            wd.find_element_by_class_name('').click()
            wd.find_element_by_id('').text

        except NoSuchElementException:
            logging.exception('error log')

        finally:
            wd.quit()


if __name__ == '__main__':
    unittest.main()