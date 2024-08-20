
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

#css chrome dev tool java = $$("#<value of id>") ex: $$("#twotabsearchtextbox")

# find by css, using ID:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox") # same thing as -> driver.find_element(By.ID, "twotabsearchtextbox")
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox") # if want to add tag of element (input) put before the "#" but ID's are unique so this is unneeded

# Find by css, using classes: can use classes too. in order to use, put a period $$(".<class name>")
# to add second part of class just add another period
# order dosnt matter
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute")
driver.find_element(By.CSS_SELECTOR, "nav-input.nav-progressive-attribute") #multiple  classes
# tag + classes
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute.nav-input")
# syntax = tag, id, classes, then others
#again add as many classes as hyou need if element has multiple classes seperated by spaces
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-progressive-attribute.nav-input")

#if want to use attribute use brackets $$("[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']") #attributes can be in any order
# tag + attributes
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][type='text']")
# tag + attributes + [attribute]
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon'][type='text']")
# for ID' use #
# for classes us .
# everything else us []

#attributes, partial matches - add astrisk after "="
driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search Ama']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_sigin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[class*='ap_sigin_notification_privacy_notice']")

# Multiple notes, parent -> child
# can sperate using space
# can be anywhere in the structure ( can  go  up in the dop  tree or down)
# $$("div.a-box div#legalTextRow") and $$("div.a-box div#legalTextRow a[href*='condition]")
driver.find_element(By.CSS_SELECTOR, "div#legaltextrow a[href*='ap_sigin_notification_privacy_notice']")

#scc selectors dont support text. to use text you must use Xpath
#supports parent -> child does not support child -> parent
