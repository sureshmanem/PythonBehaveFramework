from gettext import find
from turtle import title
from behave import given, when, then

# from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@given("Launch Chrome Browser")
def step_impl(context):
    driver.get("https://www.saucedemo.com/")


@when("Open the Sauce Labs Home Page")
def openHomePage(context):
    assert "Swag Labs" in driver.title


@when('Enter username as "{uname}" and password as "{pwd}"')
def step_impl(context, uname, pwd):
    driver.find_element(By.ID, "user-name").send_keys(uname)
    driver.find_element(By.ID, "password").send_keys(pwd)


@when("Click on Login button")
def step_impl(context):
    driver.find_element(By.ID, "login-button").click()


@then("Verify successful login")
def step_impl(context):
    strName = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/span"
    ).text
    assert strName == "Products"
    driver.close()
