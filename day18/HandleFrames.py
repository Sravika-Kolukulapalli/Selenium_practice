from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://vinothqaacademy.com/iframe/")
driver.maximize_window()

driver.switch_to.frame("employeetable")
driver.find_element(By.ID,"nameInput").send_keys("Sravika")
driver.find_element(By.ID,"roleInput").send_keys("Software Engineer")
driver.find_element(By.ID,"emailInput").send_keys("sravika@gmail.com")
driver.find_element(By.ID,"locationInput").send_keys("Hyderabad")
driver.find_element(By.ID,"departmentInput").send_keys("IT")
driver.find_element(By.XPATH,"//button[@id='addBtn']").click()
driver.switch_to.default_content()


driver.switch_to.frame("popuppage")
driver.find_element(By.NAME,"alertbox").click()
driver.switch_to.alert.accept()
driver.switch_to.default_content()#go back to main content

driver.switch_to.frame("registeruser")
driver.find_element(By.NAME,"vfb-5").send_keys("Sravika")
driver.find_element(By.NAME,"vfb-7").send_keys("Kolukulapalli")
driver.find_element(By.NAME,"vfb-31").click()
driver.find_element(By.NAME,"vfb-20[]").click()
driver.find_element(By.NAME,"vfb-14").send_keys("sravika@gmail.com")
driver.find_element(By.NAME,"vfb-3").send_keys("33")
driver.find_element(By.NAME,"vfb-submit").click()
