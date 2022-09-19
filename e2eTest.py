from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    if product.find_element(By.XPATH,"div/h4").text == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']/ul[1]")))
driver.find_element(By.XPATH,"//div[@class='suggestions']/ul[1]").click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()
msg = driver.find_element(By.CSS_SELECTOR,".alert").text

assert "Success! Thank you!" in msg