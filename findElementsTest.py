import time

import menu as menu
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# Here we r selecting the option from dynamic dropdownlist
driver.maximize_window()
driver.find_element(By.ID,"autosuggest").send_keys('Ind')
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
#driver.close()

#Now among the multiple options we have to select india

for country in countries:
    if country.text == "India":
        country.click()
        break

#To get the selected dropdown option

# print(driver.find_element(By.ID,"autosuggest").text) ---> To extract dynamic options it won't work

print(driver.find_element(By.ID,"autosuggest").get_attribute('value'))

assert driver.find_element(By.ID,"autosuggest").get_attribute('value') == 'India'




