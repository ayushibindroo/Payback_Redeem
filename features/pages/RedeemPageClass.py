
from selenium.webdriver.common.by import By
import time

class RedeemPageClass:


    def __init__(self, driver):
        self.driver = driver


        self.BrandNameElement = "//form[@class='d-flex align-items-center bg-white rounded']/input"
        self.SearchButtonElement = "//button[@class ='bg-white border-0 p-0 float-left py-1']"

        self.RedeemEmailPencilButtonElement="(//*[@class='position-absolute']/img)[3]"
        self.RedeemMobilePencilButtonElement="(//*[@class='position-absolute']/img)[4]"
        self.RedeemEmailTextBoxElement="//input[@name='email']"
        self.RedeemMobileTextBoxElement="//input[@name='mobile']"
        self.AddToCartButton="//button[text()='Add to cart']"
        self.PlaceOrderButton="//button[text()='Place order']"

    def enter_brandname_textbox(self, bn):
        BrandNameTextBox = self.driver.find_element(By.XPATH, self.BrandNameElement)
        BrandNameTextBox.send_keys(bn)

    def click_search_button(self):
        SearchButton = self.driver.find_element(By.XPATH, self.SearchButtonElement)
        SearchButton.click()

    def click_RedeemEmail_button(self):
        RedeemEmailButton = self.driver.find_element(By.XPATH, self.RedeemEmailPencilButtonElement)
        RedeemEmailButton.click()

    def enter_RedeemEmail_textbox(self,remail):
        RedeemEmailTextBox = self.driver.find_element(By.XPATH, self.RedeemEmailTextBoxElement)
        RedeemEmailTextBox.send_keys(remail)

    def click_RedeemMobileNumber_button(self):
        RedeemMobileNumberButton = self.driver.find_element(By.XPATH, self.RedeemMobilePencilButtonElement)
        RedeemMobileNumberButton.click()

    def enter_RedeemMobileNumber_textbox(self,remn):
        RedeemMobileNumberTextBox = self.driver.find_element(By.XPATH, self.RedeemMobileTextBoxElement)
        RedeemMobileNumberTextBox.send_keys(remn)

    def click_addtocart_button(self):
        AddtocartButton = self.driver.find_element(By.XPATH, self.AddToCartButton)
        AddtocartButton.click()

    def click_placeorder_button(self):
        PlaceorderButton = self.driver.find_element(By.XPATH, self.PlaceOrderButton)
        PlaceorderButton.click()
