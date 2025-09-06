from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/register")
###########find_element###########
# #locator matching with single element
# driver.find_element(By.NAME,"q").send_keys("Apple Macbook Pro")
#
#
# #Locator matching with multiple elements
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)#Sitemap
#
# #Element not available then throw NoSuchElementException
# login_element=driver.find_element(By.LINK_TEXT,"Log")#given wrong linktext
# login_element.click()



##############find_elements############
# #Locator matching with single webelement
# elements=driver.find_elements(By.NAME,"q")
# print(len(elements))#1
# elements[0].send_keys("Apple Macbook Pro")


#Locator matching with multiple elements
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))#23
# print(elements[0].text)#sitemap
#
# for ele in elements:
#     print(ele.text)


# #Element not available then throw NoSuchElementException
elements=driver.find_elements(By.LINK_TEXT,"Log")#given wrong linktext
print("elements returned",len(elements))#elements returned 0









