from selenium import webdriver
from selenium.webdriver.support.select import Select
from utilities import Utilities as utils


class Registration:

    def __init__(self, driver):
        self.driver = driver
        self.topframe_id = "topFrame"
        self.borrower_btn_linktext = "Borrower"
        self.mainframe_id = "mainFrame"
        self.registration_btn_linktext = "Registration"
        self.bdyload_frame_id = "bdyLoad"
        self.ssn1_textbox_name = "ssn1"
        self.ssn2_textbox_name = "ssn2"
        self.ssn3_textbox_name = "ssn3"
        self.ssn4_textbox_name = "ssn4"
        self.ssn5_textbox_name = "ssn5"
        self.ssn6_textbox_name = "ssn6"
        self.lastname_textbox_name = "customerBean.lastNm"
        self.firstname_textbox_name = "customerBean.firstNm"
        self.address_textbox_name = "customerBean.addressLn"
        self.city_textbox_name = "customerBean.city"
        self.stateid_dropdown_name = "customerBean.stateCd"
        self.zipcode_textbox_name = "customerBean.postalCd"
        self.monthsat_textbox_name = "customerBean.monthsAtAddress"

    def registration(self):
        self.driver.switch_to.frame(self.topframe_id)
        self.driver.find_element_by_link_text(self.borrower_btn_linktext).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.mainframe_id)
        self.driver.find_element_by_link_text(self.registration_btn_linktext).click()
        self.driver.switch_to.frame(self.bdyload_frame_id)
        self.driver.find_element_by_name(self.ssn1_textbox_name).send_keys(utils.ssn1)
        self.driver.find_element_by_name(self.ssn2_textbox_name).send_keys(utils.ssn2)
        self.driver.find_element_by_name(self.ssn3_textbox_name).send_keys(utils.ssn3)
        self.driver.find_element_by_name(self.ssn4_textbox_name).send_keys(utils.ssn1)
        self.driver.find_element_by_name(self.ssn5_textbox_name).send_keys(utils.ssn2)
        self.driver.find_element_by_name(self.ssn6_textbox_name).send_keys(utils.ssn3)
        self.driver.find_element_by_name(self.lastname_textbox_name).send_keys("Jack")
        self.driver.find_element_by_name(self.firstname_textbox_name).send_keys("Jones")
        self.driver.find_element_by_name(self.address_textbox_name).send_keys("109 avenue")
        self.driver.find_element_by_name(self.city_textbox_name).send_keys("NewYorkCity")
        stateid = self.driver.find_element_by_name(self.stateid_dropdown_name)
        Select(stateid).select_by_visible_text(utils.state)
        zipcode = self.driver.find_element_by_name(self.zipcode_textbox_name)
        if utils.state == "Kansas":
            zipcode.send_keys('64030')
        elif utils.state == "Missouri":
            zipcode.send_keys('63010')







