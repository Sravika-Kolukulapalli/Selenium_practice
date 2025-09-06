import pytest

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class TestLogin:
    def test_login_chrome(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    # def test_login_edge(self):
    #     self.driver = webdriver.Edge()
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     time.sleep(5)
    #     self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    #     self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    #     self.driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
    #     assert self.driver.title == "OrangeHRM"
    #     self.driver.quit()

    def test_login_firefox(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()



