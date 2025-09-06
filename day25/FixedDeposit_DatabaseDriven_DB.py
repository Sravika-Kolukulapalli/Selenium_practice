import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import mysql.connector
driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
try:
    connection = mysql.connector.connect(host="localhost", port=3306, user="root", password="Cisco1@11042002",
                                         database="db")
    curs = connection.cursor()
    curs.execute("select * from caldata")

    for row in curs:
        #reading data from database
        pric=row[0]
        roi=row[1]
        per1=row[2]
        per2=row[3]
        freq=row[4]
        exp_mvalue=row[5]
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
        else:
            print("test failed")
        driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
        time.sleep(3)
    connection.close()

except:
    print("connection unsuccessful")
driver.close()

'''Principle	Rate of Interest	Period		Frequency	Maturity Value	Expected	result
20000	10	2	year(s)	Simple Interest	24000	Pass	
40000	15	5	year(s)	Simple Interest	70000	Pass	
50000	10	3	month(s)	Simple Interest	51250	Pass	
75000	12	2	month(s)	Simple Interest	76500	Pass	
75000	12	2	day(s)	Simple Interest	75045.32	Fail	'''