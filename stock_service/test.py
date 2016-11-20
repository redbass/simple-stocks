import logging

import datetime

from stock_service import service
from stock_service.model.trade import Trade, TradeType

symbols = ["TEA", "POP", "ALE", "GIN", "JOE"]

trades = [
    Trade("TEA", TradeType.SELL,  20, 12.23),
    Trade("POP", TradeType.BUY,   80,  7.56),
    Trade("TEA", TradeType.BUY,  450, 10.20),
    Trade("POP", TradeType.SELL,  50,  6.20),
    Trade("ALE", TradeType.SELL, 214, 25.67),
    Trade("GIN", TradeType.BUY,   77,  8.97),
    Trade("JOE", TradeType.BUY,  120, 18.97),
    Trade("ALE", TradeType.BUY,   83, 21.00),
    Trade("GIN", TradeType.SELL,  70, 12.97),
    Trade("JOE", TradeType.BUY,  326, 20.97),

    Trade("TEA", TradeType.SELL,  20, 12.23),
    Trade("POP", TradeType.BUY,   80,  7.56),
    Trade("TEA", TradeType.BUY,  450, 10.20),
    Trade("POP", TradeType.SELL,  50,  6.20),
    Trade("ALE", TradeType.SELL, 214, 25.67),
    Trade("GIN", TradeType.BUY,   77,  8.97),
    Trade("JOE", TradeType.BUY,  120, 18.97),
    Trade("ALE", TradeType.BUY,   83, 21.00),
    Trade("GIN", TradeType.SELL,  70, 12.97),
    Trade("JOE", TradeType.BUY,  326, 20.97)
]


def run_app():

    for n in xrange(0, len(trades)):
        time_delay = len(trades) - n
        trade = trades[n]
        trade.timeStamp = trade.timeStamp - \
                          datetime.timedelta(minutes=time_delay)
        service.record_trade(trade)

    for symbol in symbols:
        service.calculate_dividend_yield(symbol)

    for symbol in symbols:
        service.calculate_pe_ratio(symbol)

    for symbol in symbols:
        service.calculate_stock_price(symbol)

    service.calculate_gbce()

    pass

if __name__ == "__main__":
    run_app()
