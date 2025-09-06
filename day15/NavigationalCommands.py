from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.back()#snapdeal

driver.forward()#amazon

driver.refresh()


driver.quit()
