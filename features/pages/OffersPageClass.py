from selenium.webdriver.common.by import By
class OffersPageClass:


    def __init__(self, driver):
        self.driver = driver

        self.redeemButtonElement = "//a[@data-title='Reliance Trends']"

    def click_redeem_button(self):
        redeemButton = self.driver.find_element(By.XPATH, self.redeemButtonElement)
        redeemButton.click()

    def new_window_element(self):
        parent = self.driver.current_window_handle

        # get first child window
        child = self.driver.window_handles

        for w in child:
            # switch focus to child window
            if w != parent:
                self.driver.switch_to.window(w)

