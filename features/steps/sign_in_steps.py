from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
