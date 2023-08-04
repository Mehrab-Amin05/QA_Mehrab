from behave import given, when, then


@given('Open product details page {url}')
def open_url(context, url):
    context.app.Main_page.open_sunscreen_page(url)