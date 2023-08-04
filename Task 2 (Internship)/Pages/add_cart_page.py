from Pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class add_cart(Page):
    product_to_cart = (By.XPATH, "//button[@class='product-form__submit button button--secondary button--full-width']")
    view_my_cart = (By.XPATH, "//a[contains(text(), 'View cart')]")
    checkout = (By.CSS_SELECTOR, ".button[name='checkout']")
    def add_cart(self):
        self.click(*self.product_to_cart)

    def verify_confirmation(self):
        sleep(1)
        self.wait_for_element_appear(*self.checkout)
        self.wait_for_element_clickable(*self.view_my_cart)
