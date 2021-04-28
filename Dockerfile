FROM python:3.7 as pibic

RUN apt-get -y update

# upgrade pip
RUN pip install --upgrade pip

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME

# Copying the application to container
COPY . $APP_HOME/

# Installing  flaks-cors
RUN pip install flask-cors 

# Installing dependencies
RUN pip install --user flask==0.12.0
RUN pip install -U flask-cors
RUN pip install -r requirements.txt
