from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on the column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
# Get the items into the list from browser
itemsFromTable = driver.find_elements(By.XPATH,"//tr/td[1]")
browseSortedElements=[]
for item in itemsFromTable:
    browseSortedElements.append(item.text)
newList = browseSortedElements.copy()
# sort the list of elements
browseSortedElements.sort()

#check whether tables gets sorted or not
assert browseSortedElements == newList

