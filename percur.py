from catalyst.utils.run_algo import run_algorithm
from catalyst.api import symbol
import pandas as pd

def initialize(context):
    context.bittrex = context.exchanges['bitfinex']
    context.poloniex = context.exchanges['poloniex']

    context.bittrex_trading_pair = symbol('eth_btc',  context.bittrex.name)
    context.poloniex_treading_pair = symbol('eth_btc', context.poloniex.name)

def handle_data(context, data):
    poloniex_price = data.current(context.poloniex_treading_pair, 'price')
    bittrex_price = data.current(context.bittrex_treading_pair, 'price')

    print('Data: {}'.format(data.current_dt))
    print('Poloniex: {}'.format(poloniex_price))
    print('Bittrex: {}'.format(bittrex_price))

def analyze(context):
    pass

run_algorithm(initialize=initialize,
              handle_data=handle_data,
              analyze=analyze,
              capital_base=100,
              live=false,
              base_currency='btc',
              exchange_name='bitfinex, poloniex',
              data_frequency='minute',
              start=pd.to_datetime('2022-11-02', utc=True),
              end=pd.to_datetime('2022-11-03', utc=True))
