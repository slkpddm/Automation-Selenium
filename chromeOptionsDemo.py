from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)