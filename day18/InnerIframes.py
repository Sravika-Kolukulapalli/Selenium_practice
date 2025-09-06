from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("welcome!!!!")


driver.switch_to.parent_frame()#outerframe