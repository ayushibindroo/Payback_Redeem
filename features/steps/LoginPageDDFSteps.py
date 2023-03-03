import time
from hamcrest import *
from behave import *
from selenium.webdriver.common.by import By

from datafiles import ExcelUtils
from features.pages.LoginPageClass import LoginPageClass
from features.utility.ConfigClass import ConfigClass



@when("User enters {Number} and {Pin} for first dataset")
def step_impl(context, Number, Pin):



    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")

    Number = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 1)
    Pin = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 2)

    LPage = LoginPageClass(context.driver)

    LPage.enter_mobilenumber_textbox(Number)
    time.sleep(1)

    LPage.enter_pin_textbox(Pin)
    time.sleep(1)





@step("It shows home page for first dataset")
def step_impl(context):

    time.sleep(10)
    expectedTitle = "Login to your PAYBACK Account"
    actualTitle = context.driver.title

    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


    if (expectedTitle == actualTitle):
        assert True
        print("Test is passed")
        ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 3, "Passed")
    else:
        print("Test is failed")
        ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 3, "Failed")
        assert False
        time.sleep(2)
