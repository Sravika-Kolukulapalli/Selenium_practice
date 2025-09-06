from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
username=driver.find_element(By.NAME,"q")
print("Display status: ",username.is_displayed())
print("Enable status: ",username.is_enabled())


rd_male=driver.find_element(By.ID,"gender-male")
rd_female=driver.find_element(By.ID,"gender-female")

print("default status of radio buttons")
print("male status: ",rd_male.is_selected())
print("female status: ",rd_female.is_selected())

print("after selecting radio button")
rd_male.click()
print("male status: ",rd_male.is_selected())
print("female status: ",rd_female.is_selected())
