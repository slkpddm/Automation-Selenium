# Suppose if I want to enter gmail , password and clic on the checkbox and that needs to be done automatically

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://github.com/login")

# Now to enter username and password automatically we need some locators . Selenuim is proving some locators like ID , Xpath , CSSSelector , name , Classname and linText

driver.find_element(By.ID, "login_field").send_keys("skp@gmail.com")
driver.find_element(By.ID,"password").send_keys("12345")

# We can use Xpath and CSS-Selector as locators irrespective of the others locators like name and ID
# Standard form fot Xpath is ---> //tagname[@attribute='value']
# CSS ---> tagname[attribute='value'] , #id ,.classname
driver.find_element(By.XPATH,"//input[@type='submit']").click()
msg=driver.find_element(By.CLASS_NAME,'flash').text
print(msg)

#Static dropdown
assert "Incorrect" in msg
print("Test is passed")