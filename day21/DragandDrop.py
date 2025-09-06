from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.maximize_window()

driver.find_element(By.ID, "Photo Manager").click()
driver.switch_to.frame(driver.find_element(By.XPATH, "//div//iframe[@class='demo-frame lazyloaded']"))
act=ActionChains(driver)
source_ele=driver.find_element(By.XPATH,"//img[@alt='The chalet at the Green mountain lake']")
target_ele=driver.find_element(By.XPATH,"//div[@id='trash']")

act.drag_and_drop(source_ele,target_ele).perform()



