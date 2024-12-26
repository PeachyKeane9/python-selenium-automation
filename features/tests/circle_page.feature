# Created by josephkeane at 12/22/24
Feature: Tests for Circle page UI
  # Enter feature description here

  Scenario: Verify circle page is open
    Given Open target circle page
    Then Verify target circle page URL is open


  Scenario: Verify circle page has  14 benefit cells
    Given Open target circle page
    Then Verify 14 benefit cells are shown

