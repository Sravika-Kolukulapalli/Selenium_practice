from selenium import webdriver
from selenium.webdriver.common.by import By
from LoginPageObject import LoginPage

class TestLogin:
    def test_login(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName("admin@yourstory.com")
        self.lp.setPassword("admin")
        self.lp.clickLogin()

        self.act_title=self.driver.title
        self.driver.close()
        assert self.act_title=="Dashboard / nopCommerce administration"
