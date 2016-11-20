from aetypes import Enum
from datetime import datetime


class TradeType(Enum):
    BUY = "buy"
    SELL = "sell"


class Trade(object):

    timeStamp = None
    stock_symbol = None
    type = None
    shares_quantity = 0
    price = 0.0

    def __init__(self, stock_symbol, trade_type, shares_quantity, price):

        self.timeStamp = datetime.utcnow()
        self.stock_symbol = stock_symbol

        if trade_type not in [TradeType.BUY, TradeType.SELL]:
            raise ValueError("Invalid Trade object: the type is not a valid"
                             "TradeType enum")
        self.type = trade_type

        if not shares_quantity > 0:
            raise ValueError("Invalid Trade object: 'shares quantity' have to "
                             "be grater then 0")
        self.shares_quantity = shares_quantity

        if not price > 0:
            raise ValueError("Invalid Trade object: 'price' have to be grater "
                             "then 0")
        self.price = price
