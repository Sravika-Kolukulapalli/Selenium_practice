import time

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#capture cookies from browser
cookies=driver.get_cookies()
print("size of cookies: ",len(cookies))#3


# #print details of all cookies
# for c in cookies:
#     # print(c)
#     print(c.get("name"),":",c.get("value"))


#Add new cookie to browser
driver.add_cookie({"name":"Mycookie","value":"123456"})
cookies=driver.get_cookies()
print("size of cookies after adding: ",len(cookies))#4


#Delete specific cookie from the browser
driver.delete_cookie("Mycookie")
cookies=driver.get_cookies()
print("size of cookies after deleting: ",len(cookies))





#Delete all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("size of cookies after deleting all: ",len(cookies))

#################
'''size of cookies:  3
size of cookies after adding:  4
size of cookies after deleting:  3
size of cookies after deleting all:  0'''
###################
