from random import randrange, random
from datetime import datetime, timedelta
from time import sleep

from kafka import KafkaProducer
import json
import sys


class QuoteGenerator:
    # Uso de semilla los valores de las locaciones de los ultimos 3 meses
    # viajes_prom: viajes diarios promedio
    # volatility: StdDev de viajes diarios
    #    df.groupBy($"location")
    #      .agg(stddev_pop($"viajes_prom").as("volatility"), max($"viajes_prom").as("viajes"))
    #      .orderBy($"location")
    quotes_list = [("48Q39G00+", 201694, 45326.88),
                   ("48Q39H00+", 45568, 29520),
                   ("48Q39J00+", 45920, 36298.3),
                   ("48Q3CH00+", 29064, 24481.28),
                   ("48Q3CJ00+", 116238, 37227.49),
                   ("48Q3FG00+", 38603, 14188.88)]

    def __init__(self, trading_start_at):
        self.trading_start_datetime = trading_start_at

    # considero mismo tipo de viajes, sin diferenciar semana/fds ni feriados
    def __nextMarketTime(self):
        # Sometimes it substracts 1 and generates late arriving tickers
        tick = randrange(5) - 1
        next_time = self.trading_start_datetime + timedelta(minutes=tick)
        # tomo como un dia de 9 a 20hs para poder hacer el ejercicio de cortar tiempos
        if next_time.hour > 20:
            next_time = (next_time + timedelta(days=1)).replace(hour=9, minute=0)

        self.trading_start_datetime = next_time
        return next_time

    def __signal(self):
        if randrange(2) == 0:
            return 1
        else:
            return -1

    def next_symbol(self):
        quote_idx = randrange(len(self.quotes_list) - 1)
        quote = self.quotes_list[quote_idx]

        # price = quote.price + (signal * rnd.nextDouble * quote.volatility * 3)
        price = quote[1] + (self.__signal() * random() * quote[2] * 3)

        return {
            'symbol': quote[0],
            'timestamp': self.__nextMarketTime().isoformat(),
            'price': float(f'{price:2.3f}')
        }


if __name__ == '__main__':
    # Initialization
    args = sys.argv

    if len(args) != 4:
        print(f"""
        |Usage: {args[0]} <brokers> <topics> <start_date>
        |  <brokers> is a list of one or more Kafka brokers
        |  <topic> one kafka topic to produce to
        |  <start_date> [OPTIONAL] iso timestamp from when to start producing data
        |
        |  {args[0]} kafka:9092 stocks 2017-11-11T10:00:00Z
        """)
        sys.exit(1)

    _, brokers, topic, start_date = args
    trading_start_datetime = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S%z')

    quote_gen = QuoteGenerator(trading_start_datetime)

    producer = KafkaProducer(
        bootstrap_servers=brokers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    while True:
        viajes_data = quote_gen.next_symbol()
        producer.send(topic, viajes_data)
        print(viajes_data)
        sleep(.5)
