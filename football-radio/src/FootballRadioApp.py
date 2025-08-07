#!/usr/bin/env python3
import pika
import sys
import os

parameters = pika.ConnectionParameters(
    host = 'rabbitmq',
    port=5672,
    virtual_host = 'local',
    credentials= pika.PlainCredentials('user', 'password')
)

def radioLisen():

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='football-match')

    channel.basic_consume(queue='football-match', auto_ack=True, on_message_callback=callback)

    print("Start of match.")
    channel.start_consuming()


def callback(ch, method, properties, body):
        print(f" What a magnificent {body}")

try:
    radioLisen()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
