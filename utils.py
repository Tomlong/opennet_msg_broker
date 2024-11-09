from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pika import BlockingConnection


class MQSettings(BaseSettings):
    host: str = Field('localhost', title='host')
    port: int = Field(5672, title='port')
    queue_name: str = Field('test_queue', title='queue name')
    max_retries: int = Field(5, title='max retries')
    retry_delay: int = Field(2, title='retry delay')

    model_config = SettingsConfigDict(env_prefix='MQ_')


def init_channel(connection: BlockingConnection, queue_name: str):
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    return channel
