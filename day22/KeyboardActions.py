#Ctrl+A
#Ctrl+C
#Tab
#Ctrl+V
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")

input1=driver.find_element(By.ID,"inputText1")
input2=driver.find_element(By.ID,"inputText2")

input1.send_keys("Welcome!!!!!!!")
act=ActionChains(driver)

#input1 Ctrl+a select text
act.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
time.sleep(5)

#input1 Ctrl+c copy
act.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
time.sleep(5)

#input1 Tab(press tab key to navigate to input2
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(5)
#or
# act.send_keys(Keys.TAB)

#input2 Ctrl+V paste
act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()