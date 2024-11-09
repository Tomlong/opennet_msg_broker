import pika
import time
from loguru import logger
from utils import MQSettings, init_channel
from pika.exceptions import AMQPConnectionError


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

    while True:
        time.sleep(2)
        channel.basic_publish(
            exchange='', routing_key=mq_settings.queue_name, body='Hello, World!'
        )
        logger.info(f"Send 'Hello, World!' to {mq_settings.queue_name}")


if __name__ == "__main__":
    main()
