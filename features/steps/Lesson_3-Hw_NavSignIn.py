from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page for Lesson 3.2')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
    sleep(5)


@when('Nav Drawer Click Sign In')
def nav_drawer_click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()
    sleep(5)


@then('Verify sign in form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    print('Test case passed')
