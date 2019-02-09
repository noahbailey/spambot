#!/usr/bin/env python3

# Present a signing page

import pickle 
import sys
import os

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options 


# Create webdriver object - Not headless to allow cred entry
def webdriver_init(): 
    firefox_options = Options()
    firefox_options.headless = False
    driver = webdriver.Firefox(options=firefox_options )
    return driver

# Export the cookies for <google> to a pickle file
def export_cookies(driver): 
    driver.get("https://www.google.com")
    pickle.dump(driver.get_cookies() , open("private/glogin.pkl","wb"))

def main(): 
    # Init webdriver with non-headless operation:   
    driver = webdriver_init()
    driver.get("https://accounts.google.com/ServiceLogin")
    input("Press 'Enter' to continue...")
    export_cookies(driver)
    driver.close() 
    
main()
