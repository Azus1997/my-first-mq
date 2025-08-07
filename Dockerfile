FROM python:latest

WORKDIR /home/docker-workspace/py/my-first-mq

COPY football-match football-match/
COPY football-radio football-radio/
COPY devops/run.sh .
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN chmod a+x run.sh

CMD ["./run.sh"]