from behave import given, when, then

# from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()


@given("Launch Browser")
def launchBrowser(context):
    driver.get("https://www.saucedemo.com/")


@when("Open Sauce Labs Home Page")
def openHomePage(context):
    assert "Swag Labs" in driver.title


@then("Verify that te logo is present")
def verifyLogo(context):
    status = driver.find_element(
        By.XPATH, "/html/body/div/div/div[2]/div[1]"
    ).is_displayed()
    assert status is True


@then("Close Browser")
def closeBrowser(context):
    driver.close()
