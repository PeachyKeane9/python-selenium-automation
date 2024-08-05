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

####### Continued  vid notes below ######


############################### find by id  ##################################
# best way, shortest way, easy to read it in code
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-logo-sprites')



################################# XPATH #########################################
# usde page structure  -> absolute path and relative path
# AP always goes through longpath and unstable
# relative is more reliable
# "//tagname[@attrubute='value"

driver.find_element(By.XPATH,"//input[@aria-label='Search Amazon']")

driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon']")

####################################################################
#on a tough page you can sometimes ask  the devs to add an id or identifyer
# you dont always have to use a tag... you can use "*" which searches for any tag...
# best if you have a unique attribute
#allow us to find attributes only
#driver.find_element(By.XPATH,"//*[@placeholder='Search Amazon']")

# you can combine attributes if your locator isnt specific enough or if youre
# having trouble  finding good  enough attributes
# $x("//input[@tabindex='0' and @type='text']")
#you can add as manty "ands"as much as you want

#             when we build XPATH sometimes wea also want to connect to text
# $x("//a[text()='BestSellers']")
# Sx("//tag[text()='Text']")
#                         ## text and attribute ###
 #$x("//a[text()='BestSellers' and @class='nav-a ']")
 ####################
 ##############  you can use parent then search inside parend for child ###############
# or child elements to find element
#seperate with slach slach //
# if using very long tags or very long attribute , you can use 'contains' to make the locator shorter...
# $x("//div[@id='nav-xshop']//a[contains(text(),'Best')]")
#
# #$x("//h2[contains(text(), 'under $30')]")
# $x("//div[@id='nav-xshop']//a[test()='Best Sellers']")


