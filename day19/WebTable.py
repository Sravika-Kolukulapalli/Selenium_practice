from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# #1)Count number of rows & columns
# NumOfRows=len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr'))
# NumOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
#
# print(NumOfRows,NumOfColumns)#7 4
# driver.close()

# #2)How to read spectific row and column data
#
# data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
# print(data)
# driver.close()


#3)Read all the rows and columns data
# NumOfRows=len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr'))
# NumOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
# for r in range(2,NumOfRows+1):
#     for c in range(1,NumOfColumns+1):
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data)
#     print()

#4)Read data based on condition
NumOfRows=len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr'))
NumOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
for r in range(2,NumOfRows+1):
    AuthorName=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if AuthorName=="Mukesh":
        BookName=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        Price=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(AuthorName,BookName,Price,sep="|")
    print()
driver.close()