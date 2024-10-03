from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def waitForElementToAppear(_drivers,element):
       wait = WebDriverWait(_drivers, 20)
       wait.until(expected_conditions.visibility_of_element_located(element))

