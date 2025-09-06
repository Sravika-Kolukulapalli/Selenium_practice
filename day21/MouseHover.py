import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#loging in
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
time.sleep(3)

#admin===>user management=====>users
Admin_Menu=driver.find_element(By.XPATH, "//span[text()='Admin']")

UserManagement=driver.find_element(By.XPATH, "//span[text()='User Management ']")#xpath is crct but not running

Users=driver.find_element(By.XPATH, "//a[text()='Users']//parent::li")



#MouseHover
act=ActionChains(driver)
act.move_to_element(Admin_Menu).move_to_element(UserManagement).move_to_element(Users).click().perform()