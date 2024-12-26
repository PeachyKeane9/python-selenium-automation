from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#
# @when('Click on Cart Icon')
# def click_cart_icon(context):
#     context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
#     sleep(5)
#
#
# @then('Verify "Your cart is empty" message is shown')
# def verify_cart_is_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "div[data-test=boxEmptyMsg]").text
#     assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
#     print('Test case passed')
#-----------------------------------------------------------------------#

# @then('Verify cell is present for {expected_cell}')
# def verify_present_cell(context, expected_cell):
#     cell = context.driver.find_element_by_css_selector(expected_cell)
#     assert cell.text == expected_cell
#     sleep(1)
#     context.driver.switch_to.window(context.driver.window_handles[1])
#
#
# @then('Verify correct cell URL opens for {expected_cell}')
# def verify_correct_cell_url(context, expected_cell):
#     cell = context.driver.find_element_by_css_selector(expected_cell)
#     assert cell.text == expected_cell
#     sleep(1)
#     context.driver.switch_to.window(context.driver.window_handles[0])

#
# @given('Open target circle page for Lesson 4')
# def open_cirlce_page(context):
#     context.driver.get('https://www.target.com/circle')
#
#
# @when('Verify Circle cells are shown')
# def verify_circle_cells_present(context):
#     context.driver.find_element(By.CSS_SELECTOR, '//*[@id="circle"]').click()