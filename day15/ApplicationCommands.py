from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.quit()