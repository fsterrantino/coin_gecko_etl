from kafka import KafkaProducer
from config.config import config
import json

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

def parse_data(json_str_data):
    dict_data = json.loads(json_str_data)

    stock_dict_data = {
        "time_exchange": dict_data['time_exchange'],
        "time_coinapi": dict_data['time_coinapi'],
        "uuid": dict_data['uuid'],
        "price": dict_data['price'],
        "size": dict_data['size'],
        "taker_side": dict_data['taker_side'],
        "symbol_id": dict_data['symbol_id'],
        "sequence": dict_data['sequence'],
        "type": dict_data['type'],
    }
    return stock_dict_data

def stream_to_kafka(data):

    producer = KafkaProducer(
        bootstrap_servers=config['kafka_bootstrap_servers'],
        value_serializer=json_serializer
    )

    producer.send(
        'stocks_trades_topic',
        parse_data(data)
    )