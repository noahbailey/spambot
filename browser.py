#!/usr/bin/python

# Browser subprocess

# https://www.seleniumhq.org/

import sys
import random
import pickle 
from time import sleep

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options 

# + sys.argv[1]
#rootpage = "https://www.google.com/search?q=cat+pictures"
#rootpage = 'https://youtube.com'

def webdriver_init(): 
    firefox_options = Options()
    firefox_options.headless = True 
    driver = webdriver.Firefox(options=firefox_options )
    return driver

def load_cookies(driver):
    driver.get("https://www.google.com")
    cookies = pickle.load(open("glogin.pkl", "rb"))
    for cookie in cookies: 
        driver.add_cookie(cookie) 


def webdriver_rootpage(driver,searchterm): 
    rootpage = 'https://www.google.com/search?q=' + str(searchterm)
    driver.get(rootpage)
    driver.implicitly_wait(5)
    print(driver.title)
    outputfile = driver.title.replace(' ','_') + '.png'
    driver.save_screenshot('img/' + outputfile)


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
        #links = driver.find_elements_by_xpath("//div[@id='search']//a[@href]")
        links = driver.find_elements_by_css_selector(".r a")
        randomlink = random.choice(links)
        href = randomlink.get_attribute("href")

        if not (filter_webpages(href)):
            continue
        
        try:
            randomlink.click()

        except: 
            #print("Click failed on " + randomlink.get_attribute("href"))
            #sprint("Click failed. ")
            driver.execute_script("window.history.go(-1)")
            links_clicked+=1
            continue

        sleep(2)
        driver.implicitly_wait(5)
        pagetitle = driver.title
        pageurl = driver.current_url
        print(pagetitle)
        imgname = pageurl.replace('https://','').replace('/','_').replace(' ','_') + '.png'
        driver.save_screenshot('img/' + imgname)
        driver.execute_script("window.history.go(-1)")
        sleep(1)
        driver.implicitly_wait(5)
        links_clicked+=1
        

def search(searchterm): 
    # Initialize webdriver
    driver = webdriver_init() 

    # Load login cookies from file
    load_cookies(driver)

    # Start a search: 
    webdriver_rootpage(driver, searchterm)
    
    # Try browsing subpagres of the search result: 
    try:
        webdriver_subpage(driver, 7)
    except: 
        driver.close()
