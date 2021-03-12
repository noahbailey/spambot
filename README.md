# SpamBot

![](https://img.shields.io/docker/cloud/build/noahbailey/spambot)

## Overview

Spambot is essentially an active counter-surveillance tool. Spambot performs 'data poisoning' on your search history to insert meaningless and useless data. Ultimately, the goal is to de-value and ruin targeting advertising online. 

To further damage the analytical models of Google, it will always click one of the suggestions while searching. It will also browse multiple search results quickly to damage the 'bounce rate' and 'session time' metrics that are used for search result placement. 

## How it Works

This script works by using the Alexa top 1 million domains and a list of the top 50 thousand search terms to add generic and useless search queries to your profile. 

To accomplish this, the script creates a cookie file containing a google login, then uses that cookie to stay logged into Google while running the searches from a headless browser. 

#### Disclaimer
> There is a very good chance it will find some _unsavory_ content online. I absolutely do not curate search terms so given the nature of the internet, this is almost a certainty. Please only run this script in private or an environment without any expectation of civility... 

## Running (The easy way)

To get up and running quickly, pull and run the docker container:

    docker run -it noahbailey/spambot:latest

Or, you may choose to build the container locally: 

    docker built -t "spambot" .
    docker run -it spambot"

Within moments the container will spring to life and begin surfing the web. 

```
2021-03-06 19:41:33 [SEARCHTERM] scaffolding
2021-03-06 19:41:50 [NAVIGATION] https://www.homedepot.ca/en/home/categories/tools/ladders-and-scaffolding/scaffolding.html
2021-03-06 19:42:05 [NAVIGATION] https://www.rona.ca/en/tools/ladders-stools-and-scaffolding/scaffolding-164505
...
```

## Running (The manual way)

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
