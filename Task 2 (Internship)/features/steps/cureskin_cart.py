from behave import given, when, then


@then ("Verify user is taken to the cart page")
def go_to_cart(context):
    context.app.view_cart.cart_page_verify()

