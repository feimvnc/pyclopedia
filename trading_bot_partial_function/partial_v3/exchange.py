PRICE_DATA= {
    "BTC/USD": [
        35_100_00,
        35_200_00,
        35_300_00,
        35_400_00,
        35_500_00,
        35_100_00,
        35_200_00,
        35_100_00,       
        35_000_00,       
    ],
    "ETH/USD": [
        2_100_00,
        2_200_00,
        2_300_00,
        2_400_00,
        2_500_00,
        2_100_00,
        2_200_00,
        2_100_00,       
        2_000_00,       
    ],    
}

class ExchangeConnectionError(Exception):
    """Connection error"""

class Exchange: 
    def __init__(self) -> None:
        self.connected = False 

    def connect(self) -> None:
        """Connect to the exchange"""
        print("Connecting to exchange...") 
        self.connected = True 

    def check_connection(self) -> None:
        """Check if connected"""
        if not self.connected:
            raise ExchangeConnectionError()

    def get_market_data(self, symbol: str) -> list[int]:
        """Return market prices data"""
        self.check_connection()
        return PRICE_DATA[symbol]

    def buy(self, symbol: str, amount: int) -> None:
        """Simulate buying"""
        self.check_connection()
        print(f"buying {amount} in market {symbol}")

    def sell(self, symbol: str, amount: int) -> None:
        """Simulate selling"""
        self.check_connection()
        print(f"Selling {amount} in market {symbol}.")
