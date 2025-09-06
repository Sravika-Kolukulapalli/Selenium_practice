from  selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    #Locators
    txtbox_username_id="Email"
    txtbox_password_id="Password"
    button_login_xpath="//button[normalize-space()='Login']"

    #constructor
    def __init__(self,driver):
        self.driver=driver

    #action methods
    def setUserName(self,username):
        usernametxt=self.driver.find_element(By.XPATH,self.txtbox_username_id)
        username.txt.clear()
        username.txt.send_keys(username)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.XPATH, self.txtbox_password_id)
        passwordtxt.txt.clear()
        passwordtxt.txt.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
