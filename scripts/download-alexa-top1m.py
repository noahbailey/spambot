#!/usr/bin/python

# Service 

# Retrieve the term list
#   1. Top 500 products
#   2. Top 500 google/bing searches
#   3. Top 100 websites
#   4. Top 100 celebrities
#   5. News? Headlines? 

import requests, zipfile, io

alexa_url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
alexa_raw = requests.get(alexa_url).content
alexa_zip = zipfile.ZipFile(io.BytesIO(alexa_raw))
alexa_zip.extractall() 