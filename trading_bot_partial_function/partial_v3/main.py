from platform import win32_edition
import statistics
from typing import Callable
from dataclasses import dataclass 
from functools import partial 
from exchange import Exchange 

"""
elegant approach: use partial function, make it more flexible
"""

TradingStrategyFunction = Callable[[list[int]], bool]

def should_buy_avg(prices: list[int], window_size: int) -> bool:   
    list_window = prices[-window_size:]    # use parameter
    return prices[-1] < statistics.mean(list_window)

def should_sell_avg(prices: list[int], window_size: int) -> bool: 
    list_window = prices[-window_size:]
    return prices[-1] > statistics.mean(list_window)

def should_buy_minmax(prices: list[int], min_price) -> bool:
    return prices[-1] < min_price 

def should_sell_minmax(prices: list[int], max_price) -> bool:
    return prices[-1] > max_price 

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

    # create partial functions, with suppliedd parameter window_size
    buy_strategy = partial(should_buy_avg, window_size=4)
    sell_stragegy = partial(should_sell_minmax, max_price=25_000_00)
    bot = TradingBot(
        exchange, 
        buy_strategy,
        sell_stragegy
        )
    bot.run("BTC/USD")

if __name__ == "__main__":
    main()

