import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


#Simple Alert
# driver.find_element(By.ID,"alertBtn").click()
#
# alertt=driver.switch_to.alert
# print(alertt.text)
# alertt.accept()


#Handlingmultiple browsers
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Selenium")
driver.find_element(By.XPATH,"//span//input[contains(@class,'wikipedia-search-button')]").submit()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Selenium"))
).click()
driver.find_element(By.LINK_TEXT,"Selenium in biology").click()
driver.find_element(By.LINK_TEXT,"Selenium (software)").click()
driver.find_element(By.LINK_TEXT,"Selenium disulfide").click()
driver.find_element(By.LINK_TEXT,"Selenium dioxide").click()


WindowIDs=driver.window_handles

for winid in WindowIDs:
    driver.switch_to.window(winid)
    time.sleep(5)
    print(driver.title)

driver.quit()


