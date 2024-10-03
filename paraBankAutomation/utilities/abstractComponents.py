from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper:

    def __init__(self,_drivers):
        self.driver = _drivers

    def webelement_enter(self,element,value):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(element)).send_keys(value)
    def webelement_click(self,element):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(element)).click()
    def get_element_text(self,element):
        return WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(element)).text