import time

import menu as menu
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys('ber')
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))

assert  len(results) > 0
# Items validations
predicted_list = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_list=[]
for result in results:
    actual_list.append(result.find_element(By.XPATH,"h4").text)
print(predicted_list,actual_list)
assert predicted_list==actual_list

for result in results:
    result.find_element(By.XPATH,'div/button').click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.XPATH,"//td[5]/p")
sum=0
for price in prices:
    sum=sum+int(price.text)
totalAmount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==totalAmount
driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()
wait = WebDriverWait(driver,10) # Explicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)

# Price and discount validations
totalAfterDiscount=float(driver.find_element(By.CSS_SELECTOR,'.discountAmt').text)
assert totalAfterDiscount < totalAmount

driver.find_element(By.XPATH,"//button[contains(.,'Place Order')]").click()
#country = input("Enter the country:")
driver.find_element(By.XPATH,"//select/option[@value='India']").click()
driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
driver.find_element(By.XPATH,"//button").click()





