from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

drpcountry_ele=driver.find_element(By.XPATH,"//option[text()='Afghanistan']//parent::select")
drpcountry=Select(drpcountry_ele)

##select option from the dropdown
# drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("ARG")#Argentina
# drpcountry.select_by_index(13)#index

# # #capture all the options and print them
# all_options=drpcountry.options
# print("total number of options: ",len(all_options))
# #
# for option in all_options:
#     print(option.text)
#
# # #select option from dropdown without using builtin function
# # for option in all_options:
# #     if option.text == "India":
# #         option.click()
# #         break





#######################
# driver.find_elements(By.XPATH,"//*[@id='post-2646']/div[2]/div/div/div/p/select")
# print("total number of options: ",len(all_options))


