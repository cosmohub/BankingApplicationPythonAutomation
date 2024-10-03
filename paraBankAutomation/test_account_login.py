from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from paraBankAutomation import test_base
from paraBankAutomation.test_base import waitForElementToAppear


class TestLogin:

    def test_invalid_login(self,_drivers):
        _drivers.find_element('name','username').send_keys("testuser@gmail.com")
        _drivers.find_element('name','password').send_keys("Pasword@10")
        _drivers.find_element('css selector','input[value="Log In"]').click()
        error_webelement = ('xpath','//p[@class="error"]')
        test_base.waitForElementToAppear(_drivers,error_webelement)
        account_error = _drivers.find_element('xpath','//p[@class="error"]')
        assert account_error.text == "The username and password could not be verified."

        _drivers.find_element('name', 'username').clear()
        _drivers.find_element('name', 'password').clear()
        _drivers.find_element('css selector','input[value="Log In"]').click()
        test_base.waitForElementToAppear(_drivers, error_webelement)
        account_error = _drivers.find_element('xpath', '//p[@class="error"]')
        assert account_error.text == "Please enter a username and password."

    def test_valid_login(self,_drivers):
        _drivers.find_element('name', 'username').send_keys("testuserauto")
        _drivers.find_element('name', 'password').send_keys("Password@10")
        _drivers.find_element('css selector', 'input[value="Log In"]').click()
        accountOverview = ('xpath','//h1[contains(text(),"Accounts Overview")]')
        waitForElementToAppear(_drivers,accountOverview)
        _drivers.get_full_page_screenshot_as_png("login.png")
        _drivers.find_element('link text','Log Out').click()





