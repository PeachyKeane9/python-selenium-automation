
Feature: Tests for cart functionality
  # Enter feature description here
#
  Scenario: User can verify "Your cart is empty" message is shown
    Given Open target main page
    When Click on cart Icon
    Then Verify "Your cart is empty" message is shown


  Scenario: Verify user can add item to cart
    Given Open target main page
    When Search for cooler
    Then Verify correct search results URL opens for cooler
    When Click on "add to cart" button for cooler
    And Click on "add to cart" button in side nav
    Then Verify cooler was added to cart
