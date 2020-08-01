FROM python:3.8

COPY Pipfile ./
COPY Pipfile.lock ./

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system

