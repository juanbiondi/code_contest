FROM python:3.5.2-alpine

RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/v3.5/community" >> /etc/apk/repositories

RUN apk update \
   && apk add --virtual build-dependencies \
       build-base \
   && apk add --no-cache --update \
       gcc \
       g++ \
       gfortran \
       musl-dev \
       linux-headers \
       ca-certificates \
       curl \
       openblas-dev@community \
   && apk add \
       bash \
       wget \
       nginx

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

# Config Nginx
RUN rm /etc/nginx/nginx.conf
COPY docker-config/nginx/nginx.conf /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/sites-available
RUN mkdir /etc/nginx/sites-enabled
COPY docker-config/nginx/sites-availables/default /etc/nginx/sites-available/default
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
COPY docker-config/nginx/proxy_params /etc/nginx/proxy_params

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN pip install -Iv gunicorn==19.9.0
RUN pip install -Iv gevent==1.3.6

# Adding start script
COPY docker-config/start.sh /tmp/start.sh

# Define workdir
WORKDIR /api

# Defining working directory and adding source code
COPY . /api

# Adding gunicorn config file
COPY docker-config/gunicorn.config.py /api

# Start app
EXPOSE 80
CMD ["bash", "/tmp/start.sh"]
