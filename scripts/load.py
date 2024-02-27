from kafka import KafkaConsumer
from config.config import config
import json
from aux_scripts.insert_data_into_postgres import insert_data_into_postgres

def load():
    consumer = KafkaConsumer(
        'stocks_trades_topic',
        bootstrap_servers=config['kafka_bootstrap_servers'],
        auto_offset_reset='earliest',
        group_id='consumer_group_A'
    )

    print('Starting the consumer.')

    message_counter = 0
    threshold = 5  # Set your desired threshold
    stocks_data_list = []

    for msg in consumer:
        stocks_data = json.loads(msg.value)
        print('Stocks data: {}'.format(stocks_data))

        stocks_data_list.append(stocks_data)
        message_counter += 1

        if message_counter >= threshold:
            print(f"Consumer retrieved {threshold} or more messages.")
            insert_data_into_postgres(stocks_data_list)
            stocks_data_list = []
            message_counter = 0
        else:
            print(f"Consumer retrieved less than {threshold} messages.")