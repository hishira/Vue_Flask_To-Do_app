FROM ubuntu:18.04

RUN useradd -ms /bin/bash michal

RUN apt-get update -y && \
    apt-get install -y software-properties-common gnupg2 apt-transport-https apt-utils

RUN apt-get install -y python3 \
	curl python3-pip
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
	apt-get install -y nodejs
RUN pip3 install -U Flask

USER michal
RUN mkdir -p /home/michal/projekt
WORKDIR /home/michal/projekt
COPY package*.json ./

RUN npm install

COPY . .
USER root
RUN pip3 install -U setuptools
RUN apt-get install wget 
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update
ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUn apt-get update
RUN apt-get install -y postgresql-12 postgresql-client-12 postgresql-contrib-12 gcc python3-dev libpq-dev
USER postgres
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER michal WITH SUPERUSER PASSWORD 'michal';" &&\
    createdb -O michal michal 
USER root
RUN apt-get install -y vim
RUN pip3 install psycopg2
RUN chmod 755 start.sh

RUN touch ~/.pgpass
RUN echo "localhost:5432:docker:docker:docker" >> ~/.pgpass
RUN chmod go-rwx ~/.pgpass

RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8
EXPOSE 8080
EXPOSE 5000
