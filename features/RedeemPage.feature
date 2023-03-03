Feature: Redeem Page

  Scenario: To verify user  navigate to the Redeem Page

    Given Chrome is opened and PayBack app is opened
    When User clicks on login icon
    And User enters correct valid mobile number "7006088738" and valid pin "6851" and clicks on checkbox
    And User clicks on login button
    And User lands on home page

  Scenario: To verify the Search Button on the redeem page
    Given Chrome is opened and PayBack app is opened
    When User clicks on login icon
    And User enters correct valid mobile number "7006088738" and valid pin "6851" and clicks on checkbox
    And User clicks on login button
    And User lands on home page
    And User clicks on explore button
    And User click on offers button
    And User clicks on redeem button
    And User navigates onto redeem page
    And User enters correct brand name "Fabindia"
    And User clicks on search button
    Then User navigates onto FabIndia Page


  Scenario: To verify the Add To Cart Functionality with valid data
    Given Chrome is opened and PayBack app is opened
    When User clicks on login icon
    And User enters correct valid mobile number "7006088738" and valid pin "6851" and clicks on checkbox
    And User clicks on login button
    And User lands on home page
    And User clicks on explore button
    And User click on offers button
    And User clicks on redeem button
    And User navigates onto redeem page
    And User enter "ayushibindroo10@gmail.com" and "7006088738"
    And User clicks on the Add to cart button


  Scenario Outline: To verify the Place Order Functionality with valid data
    Given Chrome is opened and PayBack app is opened
    When User clicks on login icon
    And User enters correct valid mobile number "7006088738" and valid pin "6851" and clicks on checkbox
    And User clicks on login button
    And User lands on home page
    And User clicks on explore button
    And User click on offers button
    And User clicks on redeem button
    And User navigates onto redeem page
    And User enter <Validemail> and <Validmobile number>
    And User clicks on the Place Order button

    Examples:
      |        Validemail              | Validmobile number  |
      | ayushibindroo10@gmail.com      |  7006088738         |

  Scenario Outline: To verify the Place Order Functionality with invalid data
    Given Chrome is opened and PayBack app is opened
    When User clicks on login icon
    And User enters correct valid mobile number "7006088738" and valid pin "6851" and clicks on checkbox
    And User clicks on login button
    And User lands on home page
    And User clicks on explore button
    And User click on offers button
    And User clicks on redeem button
    And User navigates onto redeem page
    And User enter <Invalidemail> and <Invalidmobile number>
    And User clicks on the Place Order button
    Then user stays on same page
    Examples:
      | Invalidemail    | Invalidmobile number  |
      | de@G.c          |  78999999             |
      | lala00.c        |  7333343              |