import statistics
from typing import Callable
from dataclasses import dataclass 

from exchange import Exchange 

"""
functional approach, use Callable to define behaviour types
improvements: removed two class types, use simple functions
disadvantages: need to use closure to pass parameters 
"""

TradingStrategyFunction = Callable[[list[int]], bool]

def should_buy_avg_closure(window_size: int) -> TradingStrategyFunction:
    def should_buy_avg(prices: list[int]) -> bool:   
        list_window = prices[-window_size:]    # use parameter
        return prices[-1] < statistics.mean(list_window)
    return should_buy_avg   

def should_sell_avg_closure(window_size: int) -> TradingStrategyFunction:
    def should_sell_avg(prices: list[int]) -> bool: 
        list_window = prices[-window_size:]
        return prices[-1] > statistics.mean(list_window)
    return should_sell_avg

def should_buy_minmax_closure(price: int) -> TradingStrategyFunction:
    def should_buy_minmax(prices: list[int]) -> bool:
        return prices[-1] < price 
    return should_buy_minmax 

def should_sell_minmax_closure(price: int) -> TradingStrategyFunction:
    def should_sell_minmax(prices: list[int]) -> bool:
        return prices[-1] > price 
    return should_sell_minmax

@dataclass 
class TradingBot:

    exchange: Exchange 
    buy_strategy: TradingStrategyFunction
    sell_strategy: TradingStrategyFunction

    def run(self, symbol: str) -> None: 
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.buy_strategy(prices)
        should_sell = self.sell_strategy(prices)
        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:
            self.exchange.sell(symbol, 10)
        else:
            print(f"No action for {symbol}")


def main() -> None: 
    exchange = Exchange()
    exchange.connect()

    bot = TradingBot(
        exchange, 
        should_buy_avg_closure(4), 
        should_sell_avg_closure(4)
        )
    bot.run("BTC/USD")

if __name__ == "__main__":
    main()

