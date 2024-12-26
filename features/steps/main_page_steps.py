from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def search_product(context):
    #find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    #click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    #wait for the page with search results to load
    sleep(6)


###############################
@when('Search for {product}')
def search_product(context, product):
    #find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys({product})
    #click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    #wait for the page with search results to load
    sleep(5)
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


