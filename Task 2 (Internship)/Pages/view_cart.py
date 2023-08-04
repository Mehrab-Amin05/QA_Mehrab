from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep
class viewcartpage(Page):
    # view_my_cart = (By.XPATH, "//a[@class='button button--secondary']")
    view_my_cart = (By.XPATH, "//a[contains(text(), 'View cart')]")
    cart_page = (By.XPATH, "//h1[contains(text(), 'Your cart')]")

    def click_view_cart(self):
        self.wait_for_element_click(*self.view_my_cart)

    def cart_page_verify(self, ):
        self.verify_element_text('Your cart', *self.cart_page)
