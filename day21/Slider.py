from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")


min_slider=driver.find_element(By.XPATH,"//span[1]")
max_slider=driver.find_element(By.XPATH,"//span[2]")

print("Location of sliders Before moving")
print(min_slider.location)#{'x': 59, 'y': 253}
print(max_slider.location)#{'x': 517, 'y': 253}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("Location of sliders After moving")
print(min_slider.location)#{'x': 160, 'y': 253}
print(max_slider.location)#{'x': 476, 'y': 253}
