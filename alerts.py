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
name1 = input("Enter the name:")
driver.find_element(By.ID,'name').send_keys(name1)
driver.find_element(By.ID,'alertbtn').click()
# javasctript popup
alert = driver.switch_to.alert
msg = alert.text
print(msg)
assert name1 in msg

alert.accept() # to click on ok
# alert.dismiss() to click on cancel

