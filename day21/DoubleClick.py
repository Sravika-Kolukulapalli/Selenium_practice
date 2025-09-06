from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Firefox()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult")

field1=driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("Welcome!!!!")

button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act=ActionChains(driver)

act.double_click(button).perform()