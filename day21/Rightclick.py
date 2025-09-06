from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()


button=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
act=ActionChains(driver)
act.context_click(button).perform()