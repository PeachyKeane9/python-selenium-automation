from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

# navigate and click 'returns and orders' page
driver.find_element(By.ID, 'nav-orders').click()

# Verify Sign in page opened
expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert expected_result == actual_result, (f'Error. Expected  text {expected_result} did not match '
                                          f'actual text{actual_result}')

# verify  email field
driver.find_element(By.XPATH, "//input[@id='ap_email']")

print('Test case passed')

driver.quit()
