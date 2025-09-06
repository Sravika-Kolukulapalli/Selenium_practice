from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#click on the link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#find total number of links
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

#print all the link names
for link in links:
    print(link.text)