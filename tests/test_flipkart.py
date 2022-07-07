import logging
import unittest
import pytest
from ddt import ddt, data, unpack, file_data

from pages.flipkart_loginpage import FkLogin
from utils.utils import Utils


@ddt
@pytest.mark.usefixtures
class TestHomepage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.lp = FkLogin(self.driver)
        self.ut = Utils()

    # @data(('9553349160', 'Lshiv@flipkart'), ('9963090928', 'Lshiv@12345'))
    # @unpack
    @file_data('..//testdata//test.json')
    def test_fk_login(self, phn, pwd):
        self.lp.phn_input(phn)
        self.lp.pwd_input(pwd)
        self.lp.login_button().click()
        # sleep(20)
        user_name = self.lp.home.username().text
        log = self.ut.custom_loggers(logLevel=logging.INFO)
        log.info(f'user has logged in as username: {user_name} is displayed')
        self.assertTrue(user_name, msg=f'{user_name} is not displayed')
        self.lp.scroll()
        self.ut.Assert(user_name, 'shivani')
