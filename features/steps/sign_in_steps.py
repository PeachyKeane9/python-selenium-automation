from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep


#Homework, Lesson  2,  3
@then('Verify sign in text displays')
def verify_sign_in_form(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    print('Test case passed')


#Homework, Lesson 2, 3
@then('Verify sign in button is shown')
def verify_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "button#login")
