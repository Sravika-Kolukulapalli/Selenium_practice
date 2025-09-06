from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

act_title=driver.title
exp_title="OrangeHRM"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")
