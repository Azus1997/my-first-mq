FROM python:latest

WORKDIR /home/docker-workspace/py/my-first-mq

COPY football-match .
COPY football-radio .
COPY devops/run.sh .

RUN chmod a+x run.sh

CMD ["./run.sh"]