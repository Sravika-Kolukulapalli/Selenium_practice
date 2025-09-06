from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get("https://demo.automationtesting.in/FileUpload.html")
driver.find_element(By.ID,"input-4").send_keys("/Users/srakoluk/Downloads/Sravika_Resume.pdf")

driver.close()

