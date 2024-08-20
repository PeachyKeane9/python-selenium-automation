# Created by josephkeane at 8/13/24
Feature: Target main page search tests
  # Enter feature description here

  Scenario User can search for a project on target
    Given Open target main page
    When Search for product
    Then Verify search worked


  Scenario: User can search for a product on target
    Given Open target main page