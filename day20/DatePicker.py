from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)#switch to frame

#mm/dd/yyyy
driver.find_element(By.ID, "datepicker").send_keys("11/04/2002")

year="2023"
month="04"
date="11"

driver.find_element(By.ID, "datepicker").click()#open datapicker

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()#next arrow
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()#previous arrow-old date


#select date
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for element in dates:
    if element.text==date:
        element.click()