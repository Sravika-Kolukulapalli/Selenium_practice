# from selenium import webdriver
#
#
# # Selenium 3
# # driver=webdriver.Chrome()
# # driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
# #
# # driver.find_element_by_name("username").send_keys("Admin")
# # driver.find_element_by_name("password").send_keys("admin123")
# # driver.find_element_by_class_name("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
# #
# #
# # act_title=driver.title
# # exp_title="OrangeHRM"
# #
# # if act_title == exp_title:
# #     print("Login test passed")
# # else:
# #     print("Login test failed")
# #
# # driver.close()

from selenium.webdriver.support import expected_conditions as EC


# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[text()=' Login ']").click()

act_title=driver.title
exp_title="OrangeHRM"

if act_title == exp_title:
    print("Test passed")
else:
    print("Test failed")






