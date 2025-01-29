from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

"""
Automated Product Price Comparison:

input a product
-option to input the websites search too? can do if implemented as a web app

output best price options on sites
"""

driver = webdriver.Chrome()  # initialize Chrome webdriver

driver.get()