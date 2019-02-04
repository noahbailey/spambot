# SearchBot

## Overview

The objective with this project is to create a system for adding 'noise' to a users' internet advertizing profile. This is essentially the only way left to retain a 'clean' profile these days, other than going outside... 

Currently this is strictly experimental, and might always be. Google has impressive neural networks fighting every second of every day to retain their competitive edge on other marketing companies, there's simply no way to compete with that type of analysis... 

## Status

Tested on the following system: 

Operating System | Python Version | Firefox Version | Status
---------------- | -------------- | --------------- | ------
Arch Linux 64bit | Python 3.7.2   | 65.0 (64bit)    | :heavy_check_mark:

## Installing

Since this script is python3, it's fairly easy to install and requires only a few additional prerequisites to run: 

### Selenium

    pip install selenium

### Gecko Driver

Gecko engine is used in this script. Download it [from Mozilla here](https://github.com/mozilla/geckodriver/releases). 

    sudo tar zxf -C /opt ./geckodriver-some-version.tar.gz
    sudo ln -s /opt/geckodriver /usr/bin/geckodriver

> This will be different if you're on Windows or MacOS...

## Running

Currently it is a standalone script. In the future it may become _more than just a script_:tm:. 

    $ ./searchbot.py

> Please don't run this as root/sudo!