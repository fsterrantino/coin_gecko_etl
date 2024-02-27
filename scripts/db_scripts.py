import psycopg2
from config.config import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database():

    db_params = {
        "host": config['postgresql']['host'],
        "port": config['postgresql']['port'],
        "user": config['postgresql']['user'],
        "password": config['postgresql']['password']
    }

    conn = psycopg2.connect(**db_params)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

    cursor = conn.cursor()

    sqlCreateDatabase = "create database coin_gecko_db;"

    try:
        cursor.execute(sqlCreateDatabase)
        print('Database created successfully')
    finally:
        cursor.close()
        conn.close()

def create_table():
    # Database connection parameters for the new database
    db_params = {
        "host": config['postgresql']['host'],
        "port": config['postgresql']['port'],
        "user": config['postgresql']['user'],
        "password": config['postgresql']['password'],
        "database": 'coin_gecko_db',  # Use the new database
    }

    # Connect to the new database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        # Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS trades (
            id SERIAL PRIMARY KEY,
            time_exchange TIMESTAMP WITH TIME ZONE,
            time_coinapi TIMESTAMP WITH TIME ZONE,
            uuid UUID,
            price NUMERIC,
            size NUMERIC,
            taker_side VARCHAR(20),
            symbol_id VARCHAR(50),
            sequence INTEGER,
            trade_type VARCHAR(20)
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully.")

    finally:
        # Close the connection
        cursor.close()
        conn.close()
