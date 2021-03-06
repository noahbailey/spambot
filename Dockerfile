FROM ubuntu:focal 

# => Stage 1: System prereqs
RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive \
        TZ=etc/UTC \
    apt-get install -y \
        firefox ca-certificates wget curl unzip python3-pip && \
    pip3 install selenium urllib3 python-slugify requests

# => Stage 2: Install Gecko webdriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz && \
    tar xzf geckodriver-v0.28.0-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver

# => Stage 3: Add scripts & data files
WORKDIR /home
RUN \
    wget http://s3.amazonaws.com/alexa-static/top-1m.csv.zip && unzip top-1m.csv.zip && \
    wget https://raw.githubusercontent.com/yabona/obfuscator/master/SERP_top && \
    mkdir -p /home/img

COPY searchbot.py /home/searchbot.py
COPY browser.py   /home/browser.py

ENTRYPOINT exec python3 searchbot.py