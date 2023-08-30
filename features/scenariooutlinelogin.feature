Feature: Sauce Labs Login using Scenario Outline

    Scenario Outline: Login to Sauce Labs with Valid multiple Parameters
        Given Launch Chrome Browser
        When Open the Sauce Labs Home Page
        And Enter username as "<username>" and password as "<password>"
        And Click on Login button
        Then Verify successful login

        Examples:
            | username      | password     |
            | standard_user | secret_sauce |

