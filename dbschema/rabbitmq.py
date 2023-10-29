import json

from aio_pika import DeliveryMode, ExchangeType, Message, connect
from aio_pika.abc import AbstractIncomingMessage
from fastapi import Request

from core.utils.custom_encoder import CustomEncoder

async def connect_to_rabbitmq(request: Request):
    """Establishes a connection to RabbitMQ using FastAPI request settings."""
    global connection
    return await connect(
        host=request.app.settings.RABBIT_MQ_HOST,
        login=request.app.settings.RABBIT_MQ_USERNAME,
        password=request.app.settings.RABBIT_MQ_PASSWORD,
        timeout=5000,
    )

async def disconnect_to_rabbitmq():
    """Closes the RabbitMQ connection."""
    await connection.close()

async def on_message(message: AbstractIncomingMessage, user_id):
    """Processes incoming RabbitMQ messages based on user ID and returns details."""
    async with message.process():
        if message.routing_key == user_id:
            return json.dumps(
                {
                    "details": message.body.decode(),
                }
            )

async def publish_rabbitmq_message(
    connection,
    routing_key,
    message_body,
    event_type,
    updated_data,
):
    """Publishes a message to RabbitMQ with specified parameters."""
    channel = await connection.channel()
    exchange = await channel.declare_exchange(
        "contact_exchange", ExchangeType.TOPIC, durable=True
    )
    message_dict_data = {
        "event_type": event_type,
        "updated_data": updated_data,
        "data": message_body,
    }
    json_data = json.dumps(message_dict_data, cls=CustomEncoder).encode("utf-8")
    message = Message(
        body=json_data,
        delivery_mode=DeliveryMode.PERSISTENT,
        headers={
            "Event-type": event_type,
            "Updated_data": updated_data,
        },
    )
    queue = await channel.declare_queue(name="contact")
    await queue.bind(exchange=exchange, routing_key=routing_key)
    await exchange.publish(message, routing_key=routing_key)