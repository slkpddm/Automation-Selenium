from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
action = ActionChains(driver)
#action.click_and_hold()
#action.double_click()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
action.context_click(driver.find_element(By.LINK_TEXT,'Top')).perform()
action.click(driver.find_element(By.ID,'mousehover')).perform()
#action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
