# Created by josephkeane at 8/13/24
Feature: Target main page search tests
  # Enter feature description here

  Scenario: User can search for tea on target
    Given Open target main page
    When Search up tea
    Then Verify search worked

###########################################################
#  Scenario: User can search for a product on target
#    Given Open target main page
#    When Search for coffee
#    Then Verify search results shown for coffee
#    And Verify correct search results URL opens for coffee
#
#
#  Scenario: User can search for a product on target
#    Given Open target main page
#    When Search for mug
#    Then Verify search results shown for mug
#    And Verify correct search results URL opens for mug
#
#
#  Scenario: User can search for a product on target
#    Given Open target main page
#    When Search for iphone
#    Then Verify search results shown for iphone
#    And Verify correct search results URL opens for iphone

  #scnario outline
  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <expected_result>
    And Verify correct search results URL opens for <expected_result>
    Examples:
    |product  |expected_result |
    |coffee   |coffee          |
    |mug      |mug             |
    |iphone   |iphone          |
##############################################################

