import os
import models
import pika
import json


def send_message_to_queue(link: str) -> None:
    connection = pika.BlockingConnection(pika.URLParameters(os.environ['RABBITMQ_URL']))
    channel = connection.channel()

    channel.queue_declare(queue='links')
    # channel.basic_consume(queue='links', auto_ack=True)
    channel.basic_publish(exchange='', routing_key='links', body=link.encode('utf-8'))

    connection.close()
