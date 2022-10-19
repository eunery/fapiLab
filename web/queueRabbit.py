import os
import models
import pika


def send_message_to_queue(link: models.Link) -> None:
    connection = pika.BlockingConnection(pika.URLParameters(os.environ['RABBITMQ_URL']))
    channel = connection.channel()

    channel.queue_declare(queue='links')
    channel.basic_consume(queue='links', auto_ack=True)
    channel.basic_publish(exchange='', routing_key='links', body=link)

    connection.close()
