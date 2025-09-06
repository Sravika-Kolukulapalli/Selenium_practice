import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#loging in
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
time.sleep(3)

#admin===>user management=====>users
driver.find_element(By.XPATH, "//span[text()='Admin']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='User Management ']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[text()='Users']//parent::li").click()
time.sleep(3)

#total rows in a table
rows=len(driver.find_elements(By.XPATH, "//div[@class='orangehrm-container']//div[@class='oxd-table-body']//div[@role='row']")[1:])
print("total number of rows in a table",rows)

count=0
for r in range(1,rows+1):
    status=driver.find_element(By.XPATH,'f"(//div[@class="oxd-table-body"]//div[@role="row"])[{r}]/div[5]"').text
    #here xpath is incorrect#we have to extract each row status
    if status=="Enabled":
        count+=1

print("Total no of rows",rows)
print("Number of enable users",count)
print("Total no of disable users",(rows-count))

driver.close()
