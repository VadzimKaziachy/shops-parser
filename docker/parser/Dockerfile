FROM python:3.9

COPY Pipfile ./
COPY Pipfile.lock ./

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system && \
    apt-get install unzip && \
    wget -N http://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip -P ~/Downloads && \
    unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads && \
    mv -f ~/Downloads/chromedriver /usr/local/share/ && \
    chmod +x /usr/local/share/chromedriver && \
    ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver && \
    ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

