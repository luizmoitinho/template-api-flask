FROM python:3.7 as report

RUN apt-get -y update

# upgrade pip
RUN pip install --upgrade pip

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME

# Copying the application to container
COPY . $APP_HOME/

# Installing dependencies
RUN pip install -r requirements.txt
