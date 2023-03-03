import time
from hamcrest import *
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePageClass import HomePageClass
from features.pages.LandingPageClass import LandingPageClass
from features.pages.LoginPageClass import LoginPageClass
from features.pages.OffersPageClass import OffersPageClass
from features.pages.RedeemPageClass import RedeemPageClass




@given(u'Chrome is opened and PayBack app is opened')
def step_impl(context):
    pass

@when(u'User clicks on login icon')
def step_impl(context):
    time.sleep(2)
    landingPage = LandingPageClass(context.driver)
    landingPage.click_login_Icon()


@when(u'User enters correct valid mobile number "{umobile}" and valid pin "{upin}" and clicks on checkbox')
def step_impl(context, umobile, upin):
    time.sleep(2)
    loginPage = LoginPageClass(context.driver)
    loginPage.enter_mobilenumber_textbox(umobile)
    time.sleep(1)
    loginPage.enter_pin_textbox(upin)
    loginPage.click_check_box()



@when(u'User clicks on login button')
def step_impl(context):
    time.sleep(2)
    loginPage = LoginPageClass(context.driver)
    loginPage.click_login_button()
    time.sleep(10)

@step("User lands on home page")
def step_impl(context):
    time.sleep(10)
    expectedTitle = "Largest Multi-brand Loyalty Program in India - PAYBACK"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(20)

@when(u'User clicks on explore button')
def step_impl(context):
    time.sleep(2)
    homepage= HomePageClass(context.driver)
    homepage.click_explore_button()


@when(u'User click on offers button')
def step_impl(context):
    time.sleep(2)
    homepage = HomePageClass(context.driver)
    homepage.click_offers_button()
    time.sleep(20)

@when(u'User clicks on redeem button')
def step_impl(context):
    time.sleep(2)
    offerspage = OffersPageClass(context.driver)
    offerspage.click_redeem_button()
    print(context.driver.title)
    offerspage = OffersPageClass(context.driver)
    offerspage.new_window_element()



@step("User navigates onto redeem page")
def step_impl(context):
    time.sleep(10)
    expectedTitle = "Get Reliance Trends Gift Vouchers & Gift Cards | Redeem Payback Points"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(20)


@when(u'User enters correct brand name "{bname}"')
def step_impl(context, bname):
    time.sleep(2)
    RedeemPage = RedeemPageClass(context.driver)
    RedeemPage.enter_brandname_textbox(bname)


@when(u'User clicks on search button')
def step_impl(context):
    time.sleep(7)
    RedeemPage = RedeemPageClass(context.driver)
    RedeemPage.click_search_button()


@then(u'User navigates onto FabIndia Page')
def step_impl(context):
    time.sleep(15)
    #expectedTitle = "Buy FabIndia Gift Vouchers & Gift Cards | Redeem Payback Points"
    expectedTitle = "Get Reliance Trends Gift Vouchers & Gift Cards | Redeem Payback Points"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(15)


@step('User enter "{uemail}" and "{umobilenumber}"')
def step_impl(context, uemail, umobilenumber):
    time.sleep(5)
    RedeemPage = RedeemPageClass(context.driver)
    RedeemPage.click_RedeemEmail_button()
    time.sleep(1)
    RedeemPage.enter_RedeemEmail_textbox(uemail)
    time.sleep(1)
    RedeemPage.click_RedeemMobileNumber_button()
    time.sleep(1)
    RedeemPage.enter_RedeemMobileNumber_textbox(umobilenumber)


@step("User clicks on the Add to cart button")
def step_impl(context):
    time.sleep(5)
    RedeemPage = RedeemPageClass(context.driver)
    RedeemPage.click_addtocart_button()


@step("User enter {uemail} and {umobilenumber}")
def step_impl(context, uemail, umobilenumber):
    time.sleep(5)
    RedeemPage = RedeemPageClass(context.driver)
    RedeemPage.click_RedeemEmail_button()
    time.sleep(1)
    RedeemPage.enter_RedeemEmail_textbox(uemail)
    time.sleep(1)
    RedeemPage.click_RedeemMobileNumber_button()
    time.sleep(1)
    RedeemPage.enter_RedeemMobileNumber_textbox(umobilenumber)


@step("User clicks on the Place Order button")
def step_impl(context):
    time.sleep(5)
    RedeemPage = RedeemPageClass(context.driver)
    RedeemPage.click_placeorder_button()



@then("user stays on same page")
def step_impl(context):
    time.sleep(5)
    print('Login Box pops')
    expectedTitle = "Get Reliance Trends Gift Vouchers & Gift Cards | Redeem Payback Points"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(5)


