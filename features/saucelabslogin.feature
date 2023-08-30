Feature: Sauce Labs Login

    Scenario: Login to Sauce Labs with Valid Parameters
        Given Launch Chrome Browser
        When Open the Sauce Labs Home Page
        And Enter username as "standard_user" and password as "secret_sauce"
        And Click on Login button
        Then Verify successful login