# Created by bavaharpreetbhalla at 4/17/22
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store original windows
    When Click on  link
    When Switch to window
    Then page is opened
    And close new window and switch back to original