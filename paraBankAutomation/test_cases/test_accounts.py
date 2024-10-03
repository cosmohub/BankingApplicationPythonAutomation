def test_login():
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    login = LoginPage(_drivers)
    login.enter_username(username)
    login.enter_password(password)
    login.submit_login()
    login.submit_logout()
