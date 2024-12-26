# Created by josephkeane at 12/22/24
Feature: Target sign in tests

  Scenario: User can navigate to sign in page
    Given Open target main page
    When Click sign in button
    And  Click sign in from side nav
    Then Verify sign in text displays
    And  Verify sign in button is shown


  Scenario: User can verify that a logged out user can navigate to Sign in
    Given Open target main page
    When Click sign in button
    When Click sign in from side nav
    Then Verify sign in text displays
    And Verify sign in button is shown

