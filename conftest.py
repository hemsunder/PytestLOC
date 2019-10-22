import pytest
from selenium import webdriver
from utilities import Utilities as utils


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type browser name eg: chrome or firefox")


@pytest.yield_fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=utils.chromepath)
    elif browser == "ie":
        driver = webdriver.Ie(executable_path=utils.iepath)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.get(utils.url)
    request.cls.driver = driver
    yield
    driver.quit()
