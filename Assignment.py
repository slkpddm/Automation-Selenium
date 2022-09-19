from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get('https://www.rahulshettyacademy.com/loginpagePractise/')
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
string = driver.find_element(By.XPATH,"//strong/a").text
print(string)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(string)
driver.find_element(By.ID,"password").send_keys("learning")
#driver.find_element(By.XPATH,"//label[2]/span[@class='checkmark']").click()
#driver.find_element(By.CSS_SELECTOR,"#cancelBtn").click()
#driver.find_element(By.CSS_SELECTOR,"#okayBtn").click()
driver.find_element(By.XPATH,"//option[@value='teach']").click()
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

