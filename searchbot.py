#!/usr/bin/python

# Service 

# Retrieve the term list
# -- Top 50,000 searches
# -- Top 1 million websites

import requests
import random 
import csv 
import os, signal 

def check_kill_process(proc): 
    for line in os.popen("ps ax | grep " + proc + " | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)

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
    if (random.randint(1,5) == 1): 
        searchterm = random.choice(top1m)[1]
    else: 
        searchterm = random.choice(serp_top)
    #print(searchterm)
    import browser 
    browser.search(searchterm)
    check_kill_process('marionette')

