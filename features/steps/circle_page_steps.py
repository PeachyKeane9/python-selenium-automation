from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# #Homework, Lesson 4
@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify target circle page URL is open')
def verify_circle_url(context):
    url = context.driver.current_url
    assert "target-circle" in url, f'Expected {"target-circle"} not in actual text {url}'

    print('Test case passed')


@then('Verify {number} benefit cells are shown')
def verify_circle_cells_amount(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, '[class="cell-item-content"]')
    assert len(cells) == number, f'Expected {number} cells but found {len(cells)}'

    print('Test case passed')
