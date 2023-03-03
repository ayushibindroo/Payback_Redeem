from selenium.webdriver.common.by import By


class LandingPageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.loginIconElement = "(//*[@class='nav-link pb-gatrack'])[4]"


    # Creating Element Methods
    def click_login_Icon(self):
        loginIcon = self.driver.find_element(By.XPATH, self.loginIconElement)
        loginIcon.click()