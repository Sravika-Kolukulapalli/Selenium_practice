from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#date of birth
driver.find_element(By.NAME, "dob").click()
datepicker_month=Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Apr")#month


datepicker_year=Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("2023")


all_dates=driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in all_dates:
    if ele.text=="25":
        ele.click()
        break



