# SearchBot

## Overview

The objective with this project is to create a system for adding 'noise' to a users' internet advertizing profile. This is essentially the only way left to retain a 'clean' profile these days, other than going outside... 

Currently this is strictly experimental, and might always be. Google has impressive neural networks fighting every second of every day to retain their competitive edge on other marketing companies, there's simply no way to compete with that type of analysis... 

#### Disclaimer
> There is a very good chance it will find some _unsavory_ content online. I absolutely do not curate search terms so given the nature of the internet, this is almost a certainty. Please only run this script in private or an environment without any expectation of civility... 

## Status

Tested on the following system: 

Operating System        | Python Version | Firefox Version | Status
----------------------- | -------------- | --------------- | ------
Arch Linux 64bit        | Python 3.7.2   | 65.0 (64bit)    | :heavy_check_mark:
Ubuntu 18.04 (Hyper-V)  | Python 3.6.7   | 65.0 (64bit)    | :heavy_check_mark:

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