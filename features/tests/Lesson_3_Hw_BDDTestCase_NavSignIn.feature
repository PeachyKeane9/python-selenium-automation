# Created by josephkeane at 8/20/24
Feature: Logged out user can navigate to Sign In
  # Enter feature description here

  Scenario: User can verify that a logged out user can navigate to Sign in
    Given Open target main page
    When Click Sign In
    When Nav Drawer Click Sign In
    Then Verify Sign In form opened

