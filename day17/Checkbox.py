from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1)select specific checkbox
# time.sleep(2)
# driver.find_element(By.ID,"monday").click()

#2)select all checkboxes
checkboxes=driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,"day")]')
print(len(checkboxes))#7

# #Approach1
# for i in range(0,len(checkboxes)):
#     checkboxes[i].click()
# #Approach2
# for checkbox in checkboxes:
#     checkbox.click()

# #3)select multiple checkboxes by my choice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute("id")
#     if weekname=='monday' or weekname=='sunday':
#         checkbox.click()

# #4)select last 2 checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()
#5)select first 2 checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

# #6)clearing all the checkboxes
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()


