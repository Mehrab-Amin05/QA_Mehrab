from Pages.Main_page import MainPage
from Pages.add_cart_page import add_cart
from Pages.view_cart import viewcartpage
# from Pages.cart_page import cart

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.Main_page = MainPage(self.driver)
        self.add_cart_page = add_cart(self.driver)
        self.view_cart = viewcartpage(self.driver)
        # self.cart_page = cart(self.driver)
