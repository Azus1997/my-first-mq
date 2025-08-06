#!/usr/bin/env python3

import random
import time
import asyncio
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost:5672'))
channel = connection.channel()

channel.queue_declare(queue='football-match')

goalChance = 0

goalCount = 0

oTime = time.time()

spentTime = time.time() - oTime


while int(spentTime) <= 15:
    goalChance = goalChance  + 7
    n = random.randint(0, 100) 
    if n < goalChance:
        goalCount = goalCount + 1
        goalChance = 0
        channel.basic_publish(exchange='', routing_key='football-match', body=('Goal!' + str(goalCount)))
                      
    time.sleep(1)

    spentTime = time.time() - oTime

channel.basic_publish(exchange='', routing_key='football-match', body=('EOM'))

connection.close()
