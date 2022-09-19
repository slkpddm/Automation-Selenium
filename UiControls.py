import time

import menu as menu
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
#Selecting checkbox
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#Selecting radiobutton
radiobuttons = driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")

for radiobutton in radiobuttons:
    if radiobutton.get_attribute('value') == 'radio2':
        radiobutton.click()
        assert  radiobutton.is_selected()
        break

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert driver.find_element(By.ID,"displayed-text").is_displayed()

driver.close()
