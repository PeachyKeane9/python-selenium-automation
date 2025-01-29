from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

    print('Test case passed')


####################################################


@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    print(actual_text)
    assert product in actual_text, f'Expected text {product} not in actual text {actual_text}'


@then('Verify correct search results URL opens for {product}')
def verify_url(context, product):
    url = context.driver.current_url
    assert product in url, f'Expected {product} not in actual text {url}'

    ##############################################


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # Always clicks on 1st Add to cart btn
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
    context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_SIDE_NAV_BTN))


@when('Click on "add to cart" button in side nav')
def side_nav_click_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN)).click()
    # context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN)
    sleep(4)


@then('verify {product} was added to cart')
def verify_item_added_to_cart(context, product):
    expected_result = "Added to cart"
    actual_result = context.driver.find_element(By.XPATH, "//span [text()='Added to cart']").text

    assert expected_result == actual_result, (f'Error. Expected  text {expected_result} did not match '
                                              f'actual text{actual_result}')
