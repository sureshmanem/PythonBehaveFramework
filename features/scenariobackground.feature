Feature: Sauce Labs Login Scenarios

    Background: Pre-Requisite Steps
        Given Launch Chrome Browser
        When Open the Sauce Labs Home Page
        And Enter username as "standard_user" and password as "secret_sauce"
        And Click on Login button
        Then Verify successful login

    Scenario: Login to Sauce Labs
        And Close Browser

    Scenario: Add to Cart
        And Click on Add To Cart
        And Close Browser

    Scenario: Remove from Cart
        And Click on Add To Cart
        And Click on Remove
        And Close Browser