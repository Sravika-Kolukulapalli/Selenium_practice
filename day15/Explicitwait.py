from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
mywait=WebDriverWait(driver,10)#explicitwait

driver.get("https://amazon.com/")
driver.maximize_window()

driver.find_element(By.NAME, "field-keywords").send_keys("laptop")
driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').submit()
searchlink= mywait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[11]/div/div/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div/img"))).click()

# driver.find_element(By.XPATH, "//span[text()='Acer Aspire Lite,13th Gen, Intel Core i3-1305U, 16GB RAM, 512GB SSD, Full HD, 15.6'/39.62cm, Windows 11 Home, Steel Gray, 1.59KG, AL15-53, Metal Body, 36 WHR, Thin and Light Premium Laptop']").click()

driver.close()