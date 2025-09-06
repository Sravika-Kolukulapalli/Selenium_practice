import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import os
driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)
driver.maximize_window()
#
# reglink=Keys.COMMAND+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)
# time.sleep(2)

# ##New Tab:Selenium4----open a new tab and witch to new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://www.orangehrm.com/")


##New window:Selenium4----open a new window and witch to new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window("window")
driver.get("https://www.orangehrm.com/")