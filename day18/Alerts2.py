from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@name='proceed']").click()
time.sleep(2)
driver.switch_to.alert.accept()


