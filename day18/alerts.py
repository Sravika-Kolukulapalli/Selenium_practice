from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()

alertwindow=driver.switch_to.alert

print(alertwindow.text)

alertwindow.send_keys("welcome")

# alertwindow.accept()#close alert window by using OK button
alertwindow.dismiss()#close alertwindow by using Cancel button




