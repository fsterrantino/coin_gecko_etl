import psycopg2
from config.config import config

def insert_data_into_postgres(list_of_stocks_dicts):

    conn = psycopg2.connect(
        host = config['postgresql']['host'],
        database = 'coin_gecko_db',
        user = config['postgresql']['user'],
        password = config['postgresql']['password']
    )

    try:
        cur = conn.cursor()
        sql = """
        INSERT INTO trades (time_exchange, time_coinapi, uuid, price, size, taker_side, symbol_id, sequence, trade_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        # Execute the SQL query
        cur.executemany(
            sql, [(
                data['time_exchange'], 
                data['time_coinapi'], 
                data['uuid'],
                
                data['price'],
                data['size'], 
                data['taker_side'],
                data['symbol_id'], 
                data['sequence'], 
                data['type']) 
                for data in list_of_stocks_dicts])

        # Commit the changes to the database
        conn.commit()
        print("Data inserted successfully!")

    except Exception as e:
        raise RuntimeError(f"Error inserting data: {e}")

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()