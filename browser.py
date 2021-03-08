#!/usr/bin/env python3

# Browser subprocess
# https://www.seleniumhq.org/

import sys
import random
import pickle 
from time import sleep
import time
from random import randint

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options 

from slugify import slugify

# --- Runtime configuration: 

hide_firefox =      False
save_screenshots =  True
use_cookies =      False

# --- Functions begin: 

# Take a screenshot of the webpage: 
def screenshot(driver): 
    imgname = "/home/img/"
    imgname += slugify(driver.title)
    imgname += '.png'
    driver.save_screenshot(imgname)
    print('[SCREENSHOT] ' +  imgname)

# Create webdriver object and start Firefox/Gecko
def webdriver_init(): 
    firefox_options = Options()
    firefox_options.headless = hide_firefox
    driver = webdriver.Firefox(options=firefox_options )
    return driver

# Import cookies previously exported
# Used to retain a session 
def load_cookies(driver):
    cookie_url = "https://www.google.com"
    driver.get(cookie_url)
    cookies = pickle.load(open("private/glogin.pkl", "rb"))
    for cookie in cookies: 
        driver.add_cookie(cookie) 
    print('[LOADCOOKIE] ' + cookie_url)


# Open google search page and type search
def webdriver_rootpage(driver,searchterm): 
    rootpage = 'https://www.google.com'
    driver.get(rootpage)
    driver.implicitly_wait(5)

    # Locate the search field and enter the search term
    searchfield = driver.find_element_by_css_selector('.gLFyf')
    for i in searchterm: 
        searchfield.send_keys(i)
        sleep(random.uniform(0.01,0.3))
    
    for i in range(randint(1,3)):
        searchfield.send_keys(Keys.DOWN)
        sleep(0.3)
    searchfield.send_keys(Keys.RETURN)

    # Output search activity to log: 
    print('[SEARCHTERM] ' + searchterm)
    
    # Wait for results page to load: 
    driver.implicitly_wait(5)
    sleep(random.uniform(5,10))

# Exclude pages that include 'google' in them
def filter_webpages(href): 
    searchable = True
    if 'google.com' in href: 
        searchable = False 
    if 'googleusercontent' in href: 
        searchable = False 
    return searchable 

# Go to subpages and 'explore' the results
def webdriver_subpage(driver,subpages): 
    if not subpages: 
        subpages = 5
    links_clicked = 0

    while links_clicked < subpages:  
        # https://stackoverflow.com/questions/20315000/select-href-with-id-and-class-using-xpath
        links = driver.find_elements_by_css_selector("div.tF2Cxc:nth-child(2) > div:nth-child(1) > a:nth-child(1)")
        randomlink = random.choice(links)
        href = randomlink.get_attribute("href")

        # Exclude irrelevant pages: 
        if not (filter_webpages(href)):
            continue
        
        # Click a result from the search page: 
        try:
            randomlink.click()
            driver.implicitly_wait(5)
            sleep(random.uniform(5,10))  

        # Go back on failed click: 
        except: 
            sleep(random.uniform(5,10))
            driver.execute_script("window.history.go(-1)")
            links_clicked+=1
            continue

        # Wait for page page to load: 

        pagetitle = driver.title
        pageurl = driver.current_url
        print('[PAGE_TITLE] ' + pagetitle)
        print('[NAVIGATION] ' + pageurl)

        # if saving screenshots is enabled, take a picture of current page: 
        if(save_screenshots):
            screenshot(driver)
        
        # When done on page, go back and prepare to click another: 
        driver.execute_script("window.history.go(-1)")
        sleep(random.uniform(2,5))
        driver.implicitly_wait(5)
        links_clicked+=1


def search(searchterm): 
    # Initialize webdriver
    driver = webdriver_init() 

    # Load login cookies from file
    if use_cookies: 
        load_cookies(driver)

    webdriver_rootpage(driver, searchterm)
    
    # Try browsing subpages of the search result: 
    try:
        webdriver_subpage(driver, 4)
    except: 
        driver.close()
        
