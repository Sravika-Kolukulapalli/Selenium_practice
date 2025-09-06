import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClass:
    @pytest.mark.parametrize('user,pwd',[("sravika_sravs_","d@143")
        ,("sravika_sravs_","admin123")
        ,("Admin","Sravs@143"),
        ("Admi","adm")
        ]
        )
    def test_login(self,user,pwd):
        self.driver=webdriver.Firefox()
        self.driver.get("https://www.instagram.com/")
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys("your_username")
        self.driver.find_element(By.NAME, "password").send_keys(pwd)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[text()='Log in']").click()
        time.sleep(1)
        try:
            self.status=self.driver.find_element(By.LINK_TEXT,"Profile").is_displayed()
            self.driver.close()
            assert self.status ==True
        except:
            self.driver.close()
            assert False