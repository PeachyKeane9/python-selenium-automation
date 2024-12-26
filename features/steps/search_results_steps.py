from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
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

#
# # # @when('Click on "add to cart" button for {product}') # # def add_to_cart(context, product): # #
# context.driver.find_element(By.CSS_SELECTOR,'[aria-label="Add Igloo Playmate Elite MaxCold 16qt Hard Sided Cooler '
# #
#
# '- Carbonite to cart"]').click() # @when('Click on "add to cart" button for cooler') # def add_to_cart(context): #
# Wait until the button is clickable #     add_to_cart_button = WebDriverWait(context.driver, 10).until( #
# EC.element_to_be_clickable((By.CSS_SELECTOR, #                                     '[aria-label="Add Igloo Playmate
# Elite MaxCold 16qt Hard Sided Cooler - Carbonite to cart"]')) #     ) #     # Click the button #
# add_to_cart_button.click()
#


# @when('Click on "add to cart" button for cooler')
# def add_to_cart(context):
#     # Find the button
#     add_to_cart_button = context.driver.find_element(By.CSS_SELECTOR,
#                                                      '[aria-label="Add Igloo Playmate Elite MaxCold 16qt Hard Sided '
#                                                      'Cooler - Carbonite to cart"]')
#
#     # Scroll into view
#     context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
#
#     # Wait for it to be clickable and then click
#     WebDriverWait(context.driver, 20).until(
#         EC.element_to_be_clickable(add_to_cart_button)
#     ).click()


@when('Click on "add to cart" button for cooler')
def add_to_cart(context):
    # Find the add-to-cart button
    add_to_cart_button = context.driver.find_element(By.CSS_SELECTOR, '[aria-label="Add Igloo Playmate Elite MaxCold '
                                                                      '16qt Hard Sided Cooler - Carbonite to cart"]')

    # Execute JavaScript to click the button
    context.driver.execute_script("arguments[0].click();", add_to_cart_button)


@when('Click on "add to cart" button in side nav')
def add_to_cart_side_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label*="Add to cart"]').click()
    sleep(5)


@then('verify {product} was added to cart')
def verify_item_added_to_cart(context, product):
    expected_result = "Added to cart"
    actual_result = context.driver.find_element(By.XPATH, "//span [text()='Added to cart']").text

    assert expected_result == actual_result, (f'Error. Expected  text {expected_result} did not match '
                                              f'actual text{actual_result}')
