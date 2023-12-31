Feature: Sauce Labs Login

    Scenario Outline: Login to Sauce Labs with multiple Parameters
        Given Launch Chrome Browser
        When Open the Sauce Labs Home Page
        And Enter username as "<uname>" and password as "<pword>"
        And Click on Login button
        Then Verify successful login
        And Close Browser

        Examples:
            | uname                   | pword        |
            | standard_user           | secret_sauce |
            | locked_out_user         | secret_sauce |
            | problem_user            | secret_sauce |
            | performance_glitch_user | secret_sauce |