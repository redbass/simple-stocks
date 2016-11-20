import logging

from stock_service.lib import functions as fn
from stock_service.lib.exceptions import UnhandledException
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
    value = fn.calculate_dividend_yield(stock)

    logging.info("The dividend yield for the stock '{symbol}' is '{value}'"
                 .format(symbol=stock_symbol, value=value))


def calculate_pe_ratio(stock_symbol):
    """
    Return the PE ratio for the given Stock Symbol
    :param stock_symbol: Stock Symbol
    """
    try:
        stock = trade_manager.get_stock(stock_symbol)
        pe = fn.calculate_pe_ratio(stock)

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
    trades = trade_manager.get_trades_in_range(stock_symbol, period)

    stock_price = fn.calculate_trades_stock_price(trades)

    logging.info("The Stock Price for the stock '{symbol}' is '{value}'"
                 .format(symbol=stock_symbol, value=stock_price))


def calculate_share_index():
    """
    The All Share Index
    """
    stock_prices = []

    def _geometric_mean(n):
        # source: http://www.jeffcomput.es/posts/2014/03/python-geometric-mean/
        return reduce(lambda x, y: x * y, n) ** (1.0 / len(n))

    for _, stock in trade_manager.get_stocks():

        trades = trade_manager.get_trades_in_range(stock.symbol)
        stock_price = fn.calculate_trades_stock_price(trades)
        if stock_price > 0:
            stock_prices.append(float(stock_price))

    share_index = _geometric_mean(stock_prices)

    logging.info("The GBCE All Share Index is '{value}'"
                 .format(value=share_index))




