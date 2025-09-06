import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from day24 import XLUtils
driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
file="/Users/srakoluk/Downloads/Caldata.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    #reading data from excel
    pric=XLUtils.readData(file,"Sheet1",r,1)
    roi=XLUtils.readData(file,"Sheet1",r,2)
    per1=XLUtils.readData(file,"Sheet1",r,3)
    per2=XLUtils.readData(file,"Sheet1",r,4)
    freq=XLUtils.readData(file,"Sheet1",r,5)
    exp_mvalue=XLUtils.readData(file,"Sheet1",r,6)
    #Passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(roi)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)

    PeriodDrop=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    PeriodDrop.select_by_visible_text(per2)

    FreqDrop=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    FreqDrop.select_by_visible_text(freq)

    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]/img').click()

    Act_matured_value=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text


    #Validation

    if float(exp_mvalue)==float(Act_matured_value):
        print("test passed")
        XLUtils.writeData(file,"Sheet1",r,8,"passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XLUtils.writeData(file,"Sheet1",r,8,"failed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
    time.sleep(3)

driver.quit()



'''Principle	Rate of Interest	Period		Frequency	Maturity Value	Expected	result
20000	10	2	year(s)	Simple Interest	24000	Pass	
40000	15	5	year(s)	Simple Interest	70000	Pass	
50000	10	3	month(s)	Simple Interest	51250	Pass	
75000	12	2	month(s)	Simple Interest	76500	Pass	
75000	12	2	day(s)	Simple Interest	75045.32	Fail	'''