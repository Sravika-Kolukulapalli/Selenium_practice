from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(3)

windows=driver.window_handles
print(f"All windows: {windows}")

driver.switch_to.window(windows[1])
print("Current window title:",driver.title)

driver.close()#it will close window[1]

driver.switch_to.window(windows[0])
print("Back to original window: ",driver.title)

time.sleep(3)


driver.quit()#it will close all windows

