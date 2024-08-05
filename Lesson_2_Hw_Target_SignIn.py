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

driver.get('https://www.target.com/')

# find sign in button and click
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

# click sign in on the right modal drawer
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()

sleep(6)

# Verify Sign in page opened
expected_result = "Sign into your Target account"
actual_result = driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text

assert expected_result == actual_result, (f'Error. Expected  text {expected_result} did not match '
                                          f'actual text{actual_result}')

# verify sign in button is shown
driver.find_element(By.ID, "login")

print('Test Case Passed')

driver.quit()
