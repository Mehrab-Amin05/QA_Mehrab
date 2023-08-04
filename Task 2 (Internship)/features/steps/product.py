from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
@when('click add to cart')
def add_to_cart(context):
    context.app.add_cart_page.add_cart()

@when ('click View cart')
def View_my_cart(context):
    context.app.view_cart.click_view_cart()
    sleep(4)

@then('Verify "added to your cart" confirmation is shown')
def verify_confirmation(context):
    context.app.add_cart_page.verify_confirmation()