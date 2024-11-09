import pika
import time
from loguru import logger
from utils import MQSettings, init_channel
from pika.exceptions import AMQPConnectionError


def callback(ch, method, properties, body):
    logger.info(f"Received msg {body}")


def main():
    mq_settings = MQSettings()
    for _ in range(mq_settings.max_retries):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=mq_settings.host, port=mq_settings.port)
            )
            channel = init_channel(connection, queue_name=mq_settings.queue_name)
            break
        except AMQPConnectionError:
            logger.error("Failed to connect to RabbitMQ, retrying...")
            time.sleep(mq_settings.retry_delay)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            time.sleep(mq_settings.retry_delay)
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_settings.host, port=mq_settings.port))
    # channel = init_channel(connection, queue_name=mq_settings.queue_name)
    channel.basic_consume(
        queue=mq_settings.queue_name, on_message_callback=callback, auto_ack=True
    )
    logger.info('start consuming')
    channel.start_consuming()
    connection.close()


if __name__ == "__main__":
    main()
