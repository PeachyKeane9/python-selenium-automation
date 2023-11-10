# LESSON 2 #

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

driver.get('https://www.amazon.com/')

# Search by ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'twotabsearchtextbox')

# Search by XPath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")

# combine multiple  attributes in xpath to specify when multiple results populate
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute' and @value='Go']")

#search Xpath using text on the page   text()
driver.find_element(By.XPATH, "//h2[text()='Try cozy styles under $50 for free']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a ']")

#contains()
driver.find_element(By.XPATH, "//h2[contains(text(),'Explore sports gifts')]")
driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Explore ') and ]")

#from parent to child (div is first element. "//" second element (inside)  a[text]
driver.find_element(By.XPATH, "//div[@id='nav-main']//a[text()='Best Sellers']")


