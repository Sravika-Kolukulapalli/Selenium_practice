from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://admin-demo.nopcommerce.com/login")

emailbox=driver.find_element(By.ID,"Email")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")

# print("result of text: ",emailbox.text)#printed nothing
# print("result of get_attribute: ",emailbox.get_attribute('value'))#abc@gmail.com

button=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button')
print("result od text: ",button.text)
print("result of get_attribute: ",button.get_attribute('type'))