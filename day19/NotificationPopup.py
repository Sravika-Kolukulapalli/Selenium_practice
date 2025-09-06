# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# ops=webdriver.ChromeOptions()
# ops.add_argument("--disable-notifications")
# driver=webdriver.Chrome(options=ops)
# driver.get("https://whatmylocation.com/")
# driver.maximize_window()



from selenium import webdriver
from selenium.webdriver.common.by import By

# Set Firefox options and preferences
ops = webdriver.FirefoxOptions()
ops.set_preference("dom.webnotifications.enabled", False)         # Disable notifications
ops.set_preference("dom.push.enabled", False)    # Disable push notifications


ops.set_preference("permissions.default.geo", 2)  # 2 = Deny, 1 = Allow, 0 = Always Ask


# Launch Firefox with options
driver = webdriver.Firefox(options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# Set Chrome preferences to block popups
# chrome_options = Options()
# prefs = {
#     "profile.default_content_setting_values.notifications": 2,  # Block notifications
#     "profile.default_content_setting_values.geolocation": 2     # Block location access
# }
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument("--disable-notifications")
#
# # Launch browser with preferences
# driver = webdriver.Chrome(options=chrome_options)
# # driver.get("https://whatmylocation.com/")
# driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_geolocation")
#
# driver.maximize_window()
# time.sleep(5)



from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Chrome(options=options)

# Override geolocation
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
    "latitude": 12.9716,
    "longitude": 77.5946,
    "accuracy": 100
})

driver.get("https://whatmylocation.com/")





