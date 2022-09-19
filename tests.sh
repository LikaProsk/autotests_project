#!/bin/bash

DOCKER_SCAN_SUGGEST=false docker build -t tests .

docker run --name tests_run --network $network tests pytest --browser $browser -n $threads

docker cp tests_run:/app/allure-report .

allure serve allure-report

docker rm tests_run