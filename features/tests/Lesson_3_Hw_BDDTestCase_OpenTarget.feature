# Created by josephkeane at 8/20/24
Feature: Verify cart is empty
  # Enter feature description here

  Scenario: User can verify "Your cart is empty" message is shown
    Given Open target main page
    When Click on Cart Icon
    Then Verify "Your cart is empty" message is shown
