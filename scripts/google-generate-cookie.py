#!/usr/bin/python

# Present a signing page

# Ideally a persistent session that can be duplicated somehow? 

import pickle 
import sys
import os

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options 



def webdriver_init(): 
    firefox_options = Options()
    firefox_options.headless = False
    driver = webdriver.Firefox(options=firefox_options )
    return driver

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