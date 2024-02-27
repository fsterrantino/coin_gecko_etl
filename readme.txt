# Coin_Gecko_ETL

## Project objective
Create an ETL process that extracts constantly Stocks information from an API with a Web Socket service, stream it to Kafka and consume and load it into a Postgres database.

## Execution
The project can be executed by anyone. It only needs Docker, being independant from local environment. With the command "docker-compose -up" you can build:
- postgre container
- airflow containers
- kafka containers
- kafdrop container (kafka monitor)
All of them are configured in the docker-compose file and already configured within the scripts to be connected successfully.

## Connections
- airflow: localhost:8080
- kafdrop: locahost:9000
- postgres: localhost:5433