import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os
driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


# driver.save_screenshot("/Users/srakoluk/PycharmProjects/Selenium/day23/screenshot1.png")
# driver.save_screenshot(os.getcwd() + "/screenshot2.png")

driver.get_screenshot_as_file(os.getcwd() + "/screenshot3.png")
# driver.get_screenshot_as_png()#screenshot in ascii format