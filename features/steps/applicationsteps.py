from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given("Launch Chrome Browser")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when("Open the Sauce Labs Home Page")
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in context.driver.title


@when('Enter username as "{username}" and password as "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)


@when("Click on Login button")
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()
    context.driver.implicitly_wait(10)


@then("Verify successful login")
def step_impl(context):
    try:
        strName = context.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/span"
        ).text
    except:
        # print(context.driver.session_id)
        assert False, "Test Failed"
    if strName == "Products":
        # print(context.driver.session_id)
        assert True, "Test Passed"


@then("Click on Add To Cart")
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()


@then("Click on Remove")
def step_impl(context):
    context.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()


@then("Close Browser")
def step_impl(context):
    context.driver.close()
