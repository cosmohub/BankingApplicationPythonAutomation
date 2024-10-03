import pytest
from paraBankAutomation.base_pages.banking_login_page import LoginPage
from paraBankAutomation.utilities.read_properties import Read_Config

def test_valid_login(_drivers):
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    login = LoginPage(_drivers)
    login.enter_username(username)
    login.enter_password(password)
    login.submit_login()
    login.submit_logout()

def test_invalid_login_empty_fields(_drivers):
    login = LoginPage(_drivers)
    login.enter_username("")
    login.enter_password("")
    login.submit_login()
    errorMessage = login.check_invalid_login_error()
    assert errorMessage == "Please enter a username and password."

def test_invalid_login_empty_password(_drivers):
    login = LoginPage(_drivers)
    login.enter_username("testuser")
    login.enter_password("")
    login.submit_login()
    errorMessage = login.check_invalid_login_error()
    assert errorMessage == "Please enter a username and password."
