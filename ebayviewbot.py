import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create headless browser
def headless_broweser():
    options = Options()
    options.headless = True
    return options

# Open and go to site
def run():
    # Open the driver
    driver = webdriver.Chrome(executable_path="Fill with path to chrome webdriver.",
                              options=headless_broweser())
    driver.get(website_URL)
    driver.close()
    return

# Get user input
print("Enter the URL: ")
website_URL = input()
print("Enter the number of views: ")
number_of_views = int(input())

# Variables
count = 0

while(count < number_of_views):
    print("Running")
    run()
    print("View:", count + 1)
    count += 1

print("Complete")










