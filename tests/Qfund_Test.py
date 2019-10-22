import pytest
from utilities import Utilities as utils
from pages.LoginPage import LoginPage
from pages.Registration import Registration


@pytest.mark.usefixtures("test_setup")
class TestQfundFeatures:

    @pytest.mark.skip
    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login(utils.username, utils.password, utils.storeid)

    def test_registration(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login(utils.username, utils.password, utils.storeid)
        reg = Registration(driver)
        reg.registration()



