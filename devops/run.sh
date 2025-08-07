#! /bin/bash

sleep 10
python3 -u /home/docker-workspace/py/my-first-mq/football-radio/src/FootballRadioApp.py &
python3 -u /home/docker-workspace/py/my-first-mq/football-match/src/FootballMatchApp.py