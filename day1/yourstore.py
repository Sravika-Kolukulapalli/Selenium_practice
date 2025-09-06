import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
driver.find_element(By.ID,"Email").clear()
time.sleep(4)
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
time.sleep(2)
driver.find_element(By.ID,"Password").clear()
time.sleep(4)
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.ID,"RememberMe").click()
driver.find_element(By.XPATH,"//button[text()='Log in']").click()
driver.find_element(By.CSS_SELECTOR,"input[type=checkbox]").click()

act_title= driver.title
exp_title="Dashboard / nopCommerce administration"

if act_title == exp_title:
    print("Login Test passed")
else:
    print("Login Test failed")

