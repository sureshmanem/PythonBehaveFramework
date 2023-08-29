Feature: Sauce Labs Logo
    Apple Sauce Labs Application Logo Feature
    Scenario: Logo Presense on Sause Labs Home Page
        Given Launch Browser
        When Open Sauce Labs Home Page
        Then Verify that te logo is present
        And Close Browser