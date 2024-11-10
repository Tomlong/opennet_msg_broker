## Description

This is the assignment 2 which is about RabbitMQ and python pika library application for the OpenNet

## Structure
- `producer.py`: Producer to send message to RabbitMQ
- `consumer.py`: Consumer to receive message from RabbitMQ
- `utils.py`: Utils for the application


### Run on docker
1. Adjust the environment variables in `docker-compose.yml` if necessary.
    - The env default values are as following.
        ```bash
        MQ_HOST=rabbitmq
        MQ_PORT=5672
        MQ_QUEUE_NAME=test_queue
        ```
2. build
    ```bash
    docker-compose build
    ```
3. run
    ```bash
    docker-compose up -d
    ```

## Demo
[demo link](https://imgur.com/a/kUXTouu)
