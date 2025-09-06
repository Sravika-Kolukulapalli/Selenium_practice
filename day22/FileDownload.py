# normal logic
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("http://demo.automationtesting.in/FileDownload.html")
# time.sleep(3)
# driver.find_element(By.XPATH, "//a[@type='button']").click()
###################################################################
#with function call to download file in default location of chrome
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# def chrome_setup():
#     driver=webdriver.Chrome()
#     return driver
#
# driver=chrome_setup()
#
# driver.get("http://demo.automationtesting.in/FileDownload.html")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(By.XPATH, "//a[@type='button']").click()
##############################################################################
# to download file in desired location

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()
# def chrome_setup():
#     preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}#used plugin to download pdf file
#     ops=webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs", preferences)
#     driver=webdriver.Chrome(options=ops)
#     return driver
#
# driver=chrome_setup()
###################################################################################
# def edge_setup():
#     preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}#have open bug for this plugin in edge to download pdf file rather than opening
#     ops=webdriver.EdgeOptions()
#     ops.add_experimental_option("prefs", preferences)
#     driver=webdriver.Edge(options=ops)
#     return driver
#
# driver=edge_setup()

################################################################################
def firefox_setup():
    preferences={"download.default_directory":location}
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.SaveToDisk", "application/msword")
    #"https://www.sitepoint.com/mime-types-complete-list/"(mime-types list)
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)#0- downloades file in desktop #1-default location(downloads) #2-desired location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True)#for pdf
    driver=webdriver.Firefox(options=ops)
    return driver

driver=firefox_setup()

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//a[@type='button']").click()
