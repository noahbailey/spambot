#!/usr/bin/env python3

# Download Amazon Alexa rankings from S3

import requests, zipfile, io

alexa_url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
alexa_raw = requests.get(alexa_url).content
alexa_zip = zipfile.ZipFile(io.BytesIO(alexa_raw))
alexa_zip.extractall() 