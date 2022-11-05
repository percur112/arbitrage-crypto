from catalyst.utils.run_algo import run_algorithm
from catalyst.api import symbol, order
import pandas as pd

def is_profitable_after_fees(sell_price, buy_price, sell_market, buy_market):
    sell_fee = get_fee(sell_market, sell_price)
    buy_fee = get_fee(buy_market, buy_price)
    expected_profit = sell_price - buy_price - sell_fee - buy_fee
    
    if expected_profit > 0:
        print("Sell {} at {}, Buy {} at {}".format(sell_market.name, sell_price)
              print("Total fees: {}".format(buy_fee + sell_fee))
              print("Expected profit: {}".format(expected_profit))
              return True
         return false

def get_fee(market, price):
    return round(market.api.fees['trading']['taker'] * price, 5)

def 

def get_adjusted_prices(price, slippage):
    adj_sell_price = price * (1 - slippage)
    adj_buy_price = price * (1 + slippage)
    return adj_sell_price, adj_buy_price
    

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
    
    if (poloniex_price > bittrex_price):
        print(" Buy on bittrex, sell on poloniex")
        order(asset=context.bittrex_treading_pair,
             amount=1,
             limit_price=bittrex_price)
        order(asset=context.poloniex_treading_pair,
             amount=1,
             limit_price=poloniex_price)
     elif (bittrex_price > ploniex_price):
        order(asset=context.bittrex_treading_pair,
             amount=1,
             limit_price=bittrex_price)
        
        order(asset=context.poloniex_treading_pair,
             amount=1,
              limit_price=poloniex_price)

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
