
Feature: Tests for cart functionality
  # Enter feature description here
#
#  Scenario: User can verify "Your cart is empty" message is shown
#    Given Open target main page
#    When Click on cart Icon
#    Then Verify "Your cart is empty" message is shown


  Scenario: Verify user can add item to cart
    Given Open target main page
    When Search for coffee
#    Then Verify correct search results URL opens for cooler
    When Click on Add to Cart button
    And Click on "add to cart" button in side nav
    Then Verify cart has 1 item(s)
