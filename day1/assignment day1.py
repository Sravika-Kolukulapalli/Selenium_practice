from selenium import webdriver
from selenium.webdriver.common.by import By


# driver=webdriver.Firefox()
# driver.get("https://admin-demo.nopcommerce.com/login")
# driver.maximize_window()
# driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
# driver.find_element(By.ID,"Password").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR,"//button[text()='Log in']").click()


driver=webdriver.Firefox()
driver.get("https://www.linkedin.com/home")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/nav/div/a[2]").click()
driver.find_element(By.ID,"username").send_keys("sravikak11@gmail.com")
driver.find_element(By.ID,"password").send_keys("Sravs@2002")
driver.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[4]/button").click()
driver.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[3]/label").click()

driver.quit()



