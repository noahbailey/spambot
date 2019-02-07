#!/usr/bin/env python3

# Browser subprocess
# https://www.seleniumhq.org/

import sys
import random
import pickle 
from time import sleep
from random import randint

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options 


def webdriver_init(): 
    firefox_options = Options()
    #firefox_options.headless = True 
    firefox_options.headless = False
    driver = webdriver.Firefox(options=firefox_options )
    return driver

def load_cookies(driver):
    driver.get("https://www.google.com")
    cookies = pickle.load(open("private/glogin.pkl", "rb"))
    for cookie in cookies: 
        driver.add_cookie(cookie) 


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
    
    # Wait for results page to load: 
    driver.implicitly_wait(5)
    sleep(random.uniform(2,5))
    print(driver.title)
    outputfile = driver.title.replace(' ','_') + '.png'

# Exclude pages that include 'google' in them
def filter_webpages(href): 
    searchable = True
    if 'google.com' in href: 
        searchable = False 
    if 'googleusercontent' in href: 
        searchable = False 
    return searchable 


def webdriver_subpage(driver,subpages): 

    if not subpages: 
        subpages = 5

    links_clicked = 0

    while links_clicked < subpages:  

        # https://stackoverflow.com/questions/20315000/select-href-with-id-and-class-using-xpath
        links = driver.find_elements_by_css_selector(".r a")
        randomlink = random.choice(links)
        href = randomlink.get_attribute("href")

        # Exclude irrelevant pages: 
        if not (filter_webpages(href)):
            continue
        
        # Click a result from the search page: 
        try:
            randomlink.click()
            driver.implicitly_wait(5)
            sleep(random.uniform(2,5))  

        # Go back on failed click: 
        except: 
            sleep(random.uniform(2,5))
            driver.execute_script("window.history.go(-1)")
            links_clicked+=1
            continue

        # Wait for page page to load: 

        pagetitle = driver.title
        pageurl = driver.current_url
        print(pagetitle)
        imgname = pageurl.replace('https://','').replace('/','_').replace(' ','_') + '.png'
        driver.save_screenshot('img/' + imgname)
        
        # When done on page, go back and prepare to click another: 
        driver.execute_script("window.history.go(-1)")
        sleep(random.uniform(2,5))
        driver.implicitly_wait(5)
        links_clicked+=1
        

def search(searchterm): 
    # Initialize webdriver
    driver = webdriver_init() 

    # Load login cookies from file
    load_cookies(driver)

    # Start a search: 
    webdriver_rootpage(driver, searchterm)
    
    # Try browsing subpages of the search result: 
    try:
        webdriver_subpage(driver, 4)
    except: 
        driver.close()
