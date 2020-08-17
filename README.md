# SearchBot

## Overview

The objective with this project is to create a system for adding useless marketing information to an Internet consumer profile. This is essentially the only way left to retain a 'clean' profile these days, other than going outside... 

## How it Works

This script works by using the Alexa top 1 million domains and a list of the top 50 thousand search terms to 'fuzz' a search engine. The ideal result of this is to add meaningless noise to a consumer profile and devalue advertisement analytics. 

To accomplish this, the script creates a cookie file containing a google login, then uses that cookie to stay logged into Google while running the searches from a headless browser. 

#### Disclaimer
> There is a very good chance it will find some _unsavory_ content online. I absolutely do not curate search terms so given the nature of the internet, this is almost a certainty. Please only run this script in private or an environment without any expectation of civility... 


## Installing

Since this script is python3, it's fairly easy to install and requires only a few additional prerequisites to run: 

### Python Prerequisites

    pip install selenium
    pip install urllib3
    pip install python-slugify

### Gecko Driver

Gecko engine is used in this script. Download it [from Mozilla here](https://github.com/mozilla/geckodriver/releases). 

    sudo tar zxf ./geckodriver-some-version.tar.gz -C /opt
    sudo ln -s /opt/geckodriver /usr/bin/

> This will be different if you're on Windows or MacOS...



## Setup

#### Generate Cookie

First, generate the Google login cookie: 

    $ ./scripts/google-generate-cookie.py

A browser will open to the google login page. Once logged in, switch back to the terminal and press enter to finish. 

In the browser window, sign into your google account so that it can add clutter to your profile. Then go back to the script and press enter to finish. 

#### Download Alexa data

Run the script to download and cache the Alexa site list: 

    $ ./scripts/download-alexa-top1m.py



## Running

Simply run the searchbot script: 

    $ ./searchbot.py

> Please don't run this as root/sudo!

## Contributing

Do you think you're smart? Do you think my code is trash? Well don't keep it to yourself! Best way to show me who the big man is, is to submit a pull request with a snarky message!
