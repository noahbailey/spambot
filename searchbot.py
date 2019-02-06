#!/usr/bin/python

# Service 

# Retrieve the term list
# -- Top 50,000 searches
# -- Top 1 million websites

import requests
import random 
import csv 


# SERP research top 50,000 list: 
print('Downloading search terms...')
top_url = 'https://raw.githubusercontent.com/yabona/obfuscator/master/SERP_top'

serp_top_raw = str((requests.get(top_url, allow_redirects=True)).content)
serp_top = str.split(serp_top_raw, '\\n')


# Alexa Top 1 million: 
top1m = []
with open('top-1m.csv') as top1m_csv: 
    reader = csv.reader(top1m_csv)
    for row in reader: 
        top1m.append(row)

while True:
    if (random.choice([True,False])): 
        searchterm = random.choice(serp_top)
    else: 
        searchterm = random.choice(top1m)[1]
    #print(searchterm)
    import browser 
    browser.search(searchterm)

