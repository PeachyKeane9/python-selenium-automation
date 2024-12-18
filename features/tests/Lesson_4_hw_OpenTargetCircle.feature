# Created by josephkeane at 10/11/24
Feature: Target Circle Page Test case

#  Scenario: Join Target Circle cell is present
#    Given Open Target circle page
#    When Search for Target Circle
#    Then Verify cell shown for Join Target Circle
#    Then Verify correct cell URL opens for Join Target Circle
#
#  Scenario: Target Circle Partners cell is present
#    Given Open Target circle page
#    When Search for Target Circle Partners
#    Then Verify cell shown for Target Circle Partners
#    Then Verify correct cell URL opens for Target Circle Partners
#
#  Scenario: See Today's Target Circle Deals cell is present
#    Given Open Target circle page
#    When Search for See Today's Target Circle Deals
#    Then Verify cell shown for Today's Target Circle Deals
#    Then Verify correct cell URL opens for See Today's Target Circle Deals
#
#  Scenario: Community Support Votes cell is present
#    Given Open Target circle page
#    When Search for Community Support Votes
#    Then Verify cell shown for Community Support Votes
#    Then Verify correct cell URL opens for Community Support Votes
#
#  Scenario: Target Circle Bonuses cell is present
#    Given Open Target circle page
#    When Search for Target Circle Bonuses
#    Then Verify cell shown for Target Circle Bonuses
#    Then Verify correct cell URL opens for Target Circle Bonuses
#
#  Scenario: Circle FAQ cell is present
#    Given Open Target circle page
#    When Search for Circle FAQ
#    Then Verify cell shown for Circle FAQ
#    Then Verify correct cell URL opens for Circle FAQ
#
#  Scenario: Find a Card Right for You cell is present
#    Given Open Target circle page
#    When Search for Find a Card Right for You
#    Then Verify cell shown for Find a Card Right for You
#    Then Verify correct cell URL opens for Find a Card Right for You
#
#  Scenario: Card FAQ cell is present
#    Given Open Target circle page
#    When Search for Card FAQ
#    Then Verify cell shown for Card FAQ
#    Then Verify correct cell URL opens for Card FAQ

  #-----------------------------------------------------------------#


#    Scenario: User can verify Cell is present
#    Given Open Target circle page
#    When Search for <cell>
#    Then Verify cell shown for <expected_cell>
#    Then Verify correct cell URL opens for <expected_cell>
#    Examples:
#    |cell                            | expected_cell                   |
#    |Join Target Circle              | Join Target Circle              |
#    |Target Circle Partners          | Target Circle Partners          |
#    |Today's Target Circle Deals     | Today's Target Circle Deals     |
#    |Community Support Votes         | Community Support Votes         |
#    |Target Circle Bonuses           | Target Circle Bonuses           |
#    |Circle FAQ                      | Circle FAQ                      |
#    |Find a Card Right for You       | Find a Card Right for You       |
#    |cell                            | expected_cell                   |
#    |Get Unlimited Same day Delivery | Get Unlimited Same day Delivery |
#    |Circle 360 FAQ                  | Circle 360 FAQ                  |

  #---------------------------------------------------------------------#

Scenario: Verify Circle cells are shown
  Given Open Target circle page
  Then Verify the 6 cells

Scenario: Verify Circle Card cells are shown
  Given Open target circle page
  Then Verify the two cells

Scenario: Verify Circle 360 cells are shown
  Given open target circle page
  Then Verify the 3 cells
