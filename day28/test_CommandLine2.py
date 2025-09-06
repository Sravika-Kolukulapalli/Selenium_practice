import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

#Generating HTML reports


class TestCLI:
    def test_logo(self,setup):
        self.driver = setup
        self.driver.get("https://www.instagram.com/")
        try:
            self.status=self.driver.find_element(By.XPATH, "//div[@id='divLogo']//img").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert self.status==False

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