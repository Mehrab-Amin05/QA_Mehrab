# Created by Owner at 7/13/2023
Feature: Checkout flow

  Scenario: User can add a product to a cart
    Given Open product details page https://shop.cureskin.com/products/sunscreen-spf-30
    When click add to cart
#    Then Verify "added to your cart" confirmation is shown
    When click View cart
    Then Verify user is taken to the cart page