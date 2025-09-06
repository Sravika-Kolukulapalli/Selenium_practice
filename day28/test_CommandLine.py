from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

#used fixture to launch browser before doing login
# class TestCLI:
#     def test_Login(self,setup):
#         self.driver = webdriver.Firefox()
#         self.driver.get("https://www.instagram.com/")
#         wait = WebDriverWait(self.driver, 10)
#         username_field = wait.until(
#             EC.presence_of_element_located((By.NAME, "username")))
#         username_field.send_keys("Admin")
#         self.driver.find_element(By.NAME, "password").send_keys("admin123")
#         time.sleep(1)
#         self.driver.find_element(By.XPATH, "//div[text()='Log in']").click()
#         time.sleep(1)
#         try:
#             self.status = self.driver.find_element(By.LINK_TEXT, "Profile").is_displayed()
#             self.driver.close()
#             assert self.status == True
#         except:
#             self.driver.close()
#             assert False

#fixture will return any value--print(setup)
# class TestCLI:
#     def test_Login(self,setup):
#         print(setup)
#         self.driver = webdriver.Firefox()
#         self.driver.get("https://www.instagram.com/")
#         wait = WebDriverWait(self.driver, 10)
#         username_field = wait.until(
#             EC.presence_of_element_located((By.NAME, "username")))
#         username_field.send_keys("Admin")
#         self.driver.find_element(By.NAME, "password").send_keys("admin123")
#         time.sleep(1)
#         self.driver.find_element(By.XPATH, "//div[text()='Log in']").click()
#         time.sleep(1)
#         try:
#             self.status = self.driver.find_element(By.LINK_TEXT, "Profile").is_displayed()
#             self.driver.close()
#             assert self.status == True
#         except:
#             self.driver.close()
#             assert False
#########################
#How fixture will return the data
# class TestCLI:
#     def test_Login(self,setup):

#         self.driver=setup
#         self.driver.get("https://www.instagram.com/")
#         wait = WebDriverWait(self.driver, 10)
#         username_field = wait.until(
#             EC.presence_of_element_located((By.NAME, "username")))
#         username_field.send_keys("Admin")
#         self.driver.find_element(By.NAME, "password").send_keys("admin123")
#         time.sleep(1)
#         self.driver.find_element(By.XPATH, "//div[text()='Log in']").click()
#         time.sleep(1)
#         try:
#             self.status = self.driver.find_element(By.LINK_TEXT, "Profile").is_displayed()
#             self.driver.close()
#             assert self.status == True
#         except:
#             self.driver.close()
#             assert False


##################
##passing browser name as argument through command line
class TestCLI:
    def test_Login(self,setup):
        self.driver=setup
        self.driver.get("https://www.instagram.com/")
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[text()='Log in']").click()
        time.sleep(1)
        try:
            self.status = self.driver.find_element(By.LINK_TEXT, "Profile").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False

