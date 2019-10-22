from selenium import webdriver


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "loginRequestBean.userId"
        self.password_textbox_name = "loginRequestBean.password"
        self.storeid_textbox_name = "loginRequestBean.locNbr"
        self.login_btn_name = "login"

    def login(self, un, pwd, stid):
        # self.driver = webdriver.Chrome
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(un)
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(pwd)
        self.driver.find_element_by_name(self.storeid_textbox_name).send_keys(stid)
        self.driver.find_element_by_name(self.login_btn_name).click()
        title = self.driver.title
        print(title)
        assert self.driver.title == "QFund"
