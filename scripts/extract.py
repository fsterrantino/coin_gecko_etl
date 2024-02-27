from websocket import WebSocketApp
import json
from config.config import config
import time
from aux_scripts.stream_to_kafka import stream_to_kafka

def on_message(ws, message):
    print(message)
    stream_to_kafka(message)
    time.sleep(10)

def on_error(ws, error):
    print(error)
 
def on_close(ws):
    print("### closed ###")
 
def on_open(ws):

    ws.send(json.dumps({
        "type": "hello",
        "apikey": config['api_key'],
        "heartbeat": False,
        "subscribe_data_type": ["trade"],
        "subscribe_filter_asset_id": ["BTC"],
        "subscribe_update_limit_ms_exrate": 1000
    }))

def extract():
    ws = WebSocketApp("wss://ws.coinapi.io/v1",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()
 
