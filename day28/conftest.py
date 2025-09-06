#fixture creation

# import pytest
# @pytest.fixture()
# def setup():
#     print("Launching browser")

##########fixture will return value
# import pytest
# @pytest.fixture()
# def setup():
#     print("Launching browser")
#     return "firefox"
########################
#How fixture will return the data
# import pytest
# from selenium import webdriver
# @pytest.fixture()
# def setup():
#     driver = webdriver.Firefox()
#     return driver

######################
#passing browser name as argument through command line
import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    elif browser=="edge":
        driver = webdriver.Edge()
    return driver

def pytest_addoption(parser):#This will get the value from the cli
    parser.addoption("--browser")

@pytest.fixture
def browser(request):#This will return the browser value to setup method
    browser = request.config.getoption("browser")

#Customizing reHTML report
#It is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata["Project Name"] = "Instagram"
    config._metadata["Module Name"] = "Login"
    config._metadata["Tester Name"] = "sravika"

#It is hook for deleting/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)