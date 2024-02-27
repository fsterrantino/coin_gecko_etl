config = {
    'api_url': 'wss://ws.coinapi.io/v1/',
    'api_key': '0850BA8F-B2F9-4453-9FD8-F7CC90C77C53',
    'kafka_bootstrap_servers': 'kafka:9092',
    'postgresql': {
        'host': 'postgres',
        'port': '5432',
        'database': 'airflow',
        'user': 'airflow',
        'password': 'airflow'
    }
}

config['api_headers'] = {
    'Authorization': f"Bearer {config['api_key']}"
}