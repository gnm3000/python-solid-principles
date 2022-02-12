"""
Template Method Pattern

It helps you standarize a process.
In particular suitable for things where you have a fixed process but the steps in the process
may be different. 
For example, a CustomerSupportTickets. The process is fixed, but may be one case need a technical
assitent in the home of the customer, so change determinated steps in the process. 

Here the process trading is the same, check prices, check if buy or sell, and then action.
But, the strategy process may be different. 

We will implement here the template method.
"""

# now I can add More trading strategies without modify anything, only add classes.
# check_prices now is complete independent from the process im going through. 

##################### Bridge  pattern design

"""
The problem now is that currently in trading bot we have also methods for things that a tradingbot
should not really do as connecting to an exchange or get data. 

the thing bridge solve is, if you have two separated things that vary, different exchanges, different 
trading bots. give you the capabilities  of adding an extra exchange or extra tradingbot, without
to do anything other side of bridge.
Bridge allow you to have two separated class hierarchies, two variations that can change independently
from each other. 

"""

from abc import ABC,abstractmethod
from typing import List


class Exchange(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def get_market_data(self,coin:str) -> List[float]:
        pass
    
class BinanceExchange(Exchange):
    def connect(self):
        print("connecting to binance...")
    
    def get_market_data(self,coin:str) -> List[float]:
        return [10,12,18,14]

class CoinbaseExchange(Exchange):
    def connect(self):
        print("connecting to coinbase...")
    
    def get_market_data(self,coin:str) -> List[float]:
        return [192,203,240,280]
  
class TradingBot(ABC):
    
    def __init__(self,exchange: Exchange) -> None:
        self.exchange = exchange # This is the BRIDGE!
        # the connection between the tradingBot and Exchange.
        # this connection happen in an abstract level. 
        # now you can have different types of tradingBot and different
        # types of exchanges. This is the idea with Bridge Pattern.
    



    @abstractmethod
    def should_buy(self,prices: List[float]) -> bool:
        pass
    
    @abstractmethod
    def should_sell(self,prices: List[float]) -> bool:
        pass
    
    def check_prices(self,coin:str):
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
        should_buy =  self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}")
        elif should_sell:
            print(f"You should sell {coin}")
        else:
            print(f"No action needed for {coin}")

class AverageTrader(TradingBot): 
    def list_average(self,list: List[float]) -> float:
        return sum(list) / len(list)
    
    def should_buy(self,prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)
    
    def should_sell(self,prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)

class MinMaxTrader(TradingBot):
    def should_buy(self,prices: List[float]) -> bool:
        return prices[-1] == min(prices)
    
    def should_sell(self,prices: List[float]) -> bool:
        return prices[-1] == max(prices)


application = AverageTrader(CoinbaseExchange())
application.check_prices("BTC/USD")

