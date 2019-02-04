#!/usr/bin/python

# Service 

# Retrieve the term list
#   1. Top 500 products
#   2. Top 500 google/bing searches
#   3. Top 100 websites
#   4. Top 100 celebrities
#   5. News? Headlines? 

import requests
import random 

print('Downloading search terms...')
top_url = 'https://raw.githubusercontent.com/yabona/obfuscator/master/SERP_top'

serp_top_raw = str((requests.get(top_url, allow_redirects=True)).content)
serp_top = str.split(serp_top_raw, '\\n')


while True:
    searchterm = random.choice(serp_top)
    print(searchterm)
    import browser 
    browser.search(searchterm)

