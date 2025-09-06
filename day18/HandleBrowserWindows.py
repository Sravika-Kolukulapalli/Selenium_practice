from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowid=driver.current_window_handle
# print(windowid) #e29f453f-f486-43c6-8ccb-efae77217c20
#                 #6000163a-0b56-49d7-9b74-78d4d30def0a


driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
WindowsIDs=driver.window_handles
# print(WindowsID)#['43cab568-8fdd-49cb-aed6-e40a093d548b', '0931bd5e-e972-474f-b14f-78644484ae05']


#Approach1
# parentwindowID=WindowsIDs[0]
# childwindowID=WindowsIDs[1]
# # print(parentwindowID)
# # print(childwindowID)
#
# driver.switch_to.window(childwindowID)
# time.sleep(5)
# print(driver.title)
#
#
# driver.switch_to.window(parentwindowID)
# print(driver.title)


# #Approach2
# for winid in WindowsIDs:
#     driver.switch_to.window(winid)
#     time.sleep(5)
#     print(driver.title)


#close specific browser
for winid in WindowsIDs:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM":
        driver.close()
