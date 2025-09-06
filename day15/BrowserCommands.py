import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

time.sleep(3)
windows=driver.window_handles
driver.switch_to.window(windows[1])
driver.close()#closes the first opened browser
# driver.quit()#close all browsers



