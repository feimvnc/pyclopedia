import statistics
from typing import Protocol 
from dataclasses import dataclass 

from exchange import Exchange 

"""
OOP approach, use class to define state and behaviours
"""

class TradingStrategy(Protocol):
    """Trading strategy to decide to sell or buy"""

    def should_buy(self, prices: list[int]) -> bool:
        raise NotImplemented 

    def should_sell(self, prices: list[int]) -> bool:
        raise NotImplementedError 

class AverageTradingStrategy:
    def should_buy(self, prices: list[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, prices: list[int]) -> bool:
        list_window = prices[-3]
        return prices[-1] > statistics.mean(list_window)

class MinMaxTradingStrategy:
    def should_buy(self, prices: list[int]) -> bool:
        return prices[-1] < 32_000_00

    def should_sell(self, prices: list[int]) -> bool:
        return prices[-1] > 32_000_00

@dataclass 
class TradingBot:

    exchange: Exchange 
    trading_strategy: TradingStrategy 

    def run(self, symbol: str) -> None: 
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.trading_strategy.should_buy(prices)
        should_sell = self.trading_strategy.should_sell(prices)
        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:
            self.exchange.sell(symbol, 10)
        else:
            print(f"No action for {symbol}")


def main() -> None: 
    exchange = Exchange()
    exchange.connect()

    trading_strategy = MinMaxTradingStrategy()

    bot = TradingBot(exchange, trading_strategy)
    bot.run("BTC/USD")

if __name__ == "__main__":
    main()

