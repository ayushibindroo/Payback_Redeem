Feature: PB Login
  Scenario: Validate PayBack login functionality on chrome
    Given Chrome is opened and PayBack app is opened
    When User clicks on login icon
    When User enters <Number> and <Pin> for first dataset
    And User clicks on login button
    And It shows home page for first dataset
