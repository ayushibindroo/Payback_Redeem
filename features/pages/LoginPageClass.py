from selenium.webdriver.common.by import By
import time
class LoginPageClass:


    def __init__(self, driver):
        self.driver = driver

        self.MobileNumberTextBoxElement = "card_number"
        self.PinTextBoxElement = "pin_number"
        #self.checkBoxButtonElement = "//div[@class='recaptcha-checkbox-border']"
        self.frameElement = "iframe"
        self.checkBoxButtonElement= "//div[@class='recaptcha-checkbox-border']"
        self.loginButtonElement = "//button[text()='LOGIN']"

    def enter_mobilenumber_textbox(self, um):
        MobileNumberTextBox = self.driver.find_element(By.NAME, self.MobileNumberTextBoxElement)
        MobileNumberTextBox.send_keys(um)

    def enter_pin_textbox(self, pn):
        PinTextBox = self.driver.find_element(By.NAME, self.PinTextBoxElement)
        PinTextBox.send_keys(pn)

    def click_check_box(self):
        iframeElement= self.driver.find_element(By.TAG_NAME, self.frameElement)
        self.driver.switch_to.frame(iframeElement)
        checkBoxButton = self.driver.find_element(By.XPATH, self.checkBoxButtonElement)
        checkBoxButton.click()
        time.sleep(20)
        self.driver.switch_to.default_content()


    def click_login_button(self):
        loginButton = self.driver.find_element(By.XPATH, self.loginButtonElement)
        loginButton.click()