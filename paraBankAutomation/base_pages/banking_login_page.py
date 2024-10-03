from selenium.webdriver.common.by import By
from selenium import webdriver
from paraBankAutomation.utilities.abstractComponents import Helper


class LoginPage(Helper):

    def __init__(self, _drivers):
        super().__init__(_drivers)
        self.driver = _drivers
        self.login_username_name = (By.NAME, "username")
        self.login_password_txtbox = (By.NAME, "password")
        self.login_submit_btn = (By.CSS_SELECTOR,"input[value='Log In']")
        self.login_error_field = (By.XPATH,"//p[@class='error']")
        self.logout_link = (By.LINK_TEXT,"Log Out")

    def enter_username(self,value):
        self.webelement_enter(self.login_username_name,value)

    def enter_password(self,value):
        self.webelement_enter(self.login_password_txtbox,value)

    def submit_login(self):
        self.webelement_click(self.login_submit_btn)

    def check_invalid_login_error(self):
        return self.get_element_text(self.login_error_field)

    def submit_logout(self):
        self.webelement_click(self.logout_link)