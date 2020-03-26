#! /bin/bash

/etc/init.d/postgresql start
touch ~/.pgpass
echo "localhost:5432:docker:docker:docker" >> ~/.pgpass
chmod go-rwx ~/.pgpass
sleep(2000)
psql -h localhost -U docker docker < database.sql

