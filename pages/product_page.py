from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def confirmation_message_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert product_name.text == added_product_name.text, "Wrong added product name"

    def basket_total_correct(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert product_cost.text == basket_total.text, "Wrong basket total"