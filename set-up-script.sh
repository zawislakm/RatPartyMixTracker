#!/bin/bash


git checkout master
git pull origin master

docker compose down
docker compose up --build -d