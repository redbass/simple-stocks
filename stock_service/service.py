import logging

from stock_service.lib.exceptions import UnhandledException
from stock_service.lib.functions import calculate_trades_stock_price, \
    get_trades_in_range
from stock_service.model.manager import TradeManager

trade_manager = TradeManager()


def record_trade(trade):
    """
    Add a new trade
    """
    trade_manager.record_trade(trade)
    logging.info("A new trade of '{symbol}' has been added"
                 .format(symbol=trade.stock_symbol))


def calculate_dividend_yield(stock_symbol):
    """
    returns the dividend yield of the given stock symbol
    :param stock_symbol:
    """
    stock = trade_manager.get_stock(stock_symbol)
    value = stock.get_dividend_yield()

    logging.info("The dividend yield for the stock '{symbol}' is '{value}'"
                 .format(symbol=stock_symbol, value=value))


def calculate_pe_ratio(stock_symbol):
    """
    Return the PE ratio for the given Stock Symbol
    :param stock_symbol: Stock Symbol
    """
    try:
        stock = trade_manager.get_stock(stock_symbol)
        pe = stock.get_pe_ratio()

        logging.info("The P/E ratio for the stock '{symbol}' is '{value}'"
                     .format(symbol=stock_symbol, value=pe))

    except UnhandledException as ex:
        logging.warn(ex.message)


def calculate_stock_price(stock_symbol, period=15):
    """
    Return the Stock price for a given symbol
    :param stock_symbol:
    :param period:
    """

    stock_price = calculate_trades_stock_price(stock_symbol, period)

    logging.info("The Stock Price for the stock '{symbol}' is '{value}'"
                 .format(symbol=stock_symbol, value=stock_price))


def calculate_gbce():
    """
    The GBCE All Share Index
    """
    stock_prices = []

    def _geometric_mean(n):
        # source: http://www.jeffcomput.es/posts/2014/03/python-geometric-mean/
        return reduce(lambda x, y: x * y, n) ** (1.0 / len(n))

    for _, stock in trade_manager.get_stocks():

        trades = get_trades_in_range(stock_symbol, 0)


        stock_price = calculate_trades_stock_price(trades)
        if stock_price > 0:
            stock_prices.append(float(stock_price))

    gbce = _geometric_mean(stock_prices)

    logging.info("The GBCE All Share Index is '{value}'".format(value=gbce))




