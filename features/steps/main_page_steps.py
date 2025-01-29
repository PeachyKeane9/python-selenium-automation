from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


Search_Btn = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


@when('Search up tea')
def search_product(context):
    # Find the search field and enter 'tea'
    context.driver.find_element(By.ID, 'search').send_keys('tea')

    # Click the search button using the Tea_product locator
    context.driver.find_element(*Search_Btn).click()

    # Wait for the page with search results to load
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(Search_Btn))


###############################


@when('Search for {product}')
def search_product(context, product):
    #find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys({product})
    #click search
    context.driver.find_element(*Search_Btn).click()
    #wait for the page with search results to load
    WebDriverWait(context.driver,10).until(EC.element_to_be_clickable(Search_Btn))
    sleep(10)

################################

# Homework, Lesson 3
@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()


#Homework, Lesson 2, 3
@when('Click sign in button')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
    sleep(5)


#Homework, Lesson 2, 3
@when('Click sign in from side nav')
def nav_drawer_click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()
    sleep(5)
