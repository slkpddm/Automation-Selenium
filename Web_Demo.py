from selenium import webdriver

#Chrome driver

# Chrome
#from selenium.webdriver.chrome.service import Service
#service_obj = Service(r"C:\Selenium files\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

#Microsoft Edge
from selenium.webdriver.edge.service import Service
service_obj = Service(r"C:\Users\gurup\Downloads\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://www.cricbuzz.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.cricbuzz.com/live-cricket-scores/51245/afg-vs-pak-super-four-match-4-a2-v-b2-asia-cup-2022")
driver.back()
driver.refresh()
driver.minimize_window()
driver.forward()
#driver.close()
