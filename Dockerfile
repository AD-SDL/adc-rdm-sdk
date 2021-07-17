FROM python:3-alpine

WORKDIR app/
COPY ./sdk .

RUN apk add --update alpine-sdk
RUN pip install -r requirements.txt


