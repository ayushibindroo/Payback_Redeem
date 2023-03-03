

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class HomePageClass:


    def __init__(self, driver):
        self.driver = driver

        self.exploreButtonElement = "//*[starts-with(text(),'Exp')]"
        self.offersButtonElement = "//a[@data-clicktext='Offers']"

    def click_explore_button(self):
        exploreButton = self.driver.find_element(By.XPATH, self.exploreButtonElement)
        action = ActionChains(self.driver)
        action.move_to_element(exploreButton)
        action.perform()

    def click_offers_button(self):
        offersButton = self.driver.find_element(By.XPATH, self.offersButtonElement)
        offersButton.click()


