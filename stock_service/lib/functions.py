from stock_service.lib.exceptions import UnhandledException
from stock_service.model.stock import StockType


def calculate_dividend_yield(stock):
    """
    Calculate the dividend yield of the given stock
    :param stock: Stock
    :return: the dividend yield
    """
    dividend_yield = -1.0

    if stock.ticker_price > 0.0:
        if stock.stock_type == StockType.COMMON:
            dividend_yield = stock.last_dividend / stock.ticker_price
        else:
            dividend_yield = \
                stock.fixed_dividend * stock.par_value / stock.ticker_price

    return dividend_yield


def calculate_pe_ratio(stock):
    """
    Calculate the P/E ratio of the given stock
    :param stock: Stock
    :return: the P/E ratio
    """
    pe_ratio = -1.0

    if stock.ticker_price > 0.0:
        dividend = calculate_dividend_yield(stock)

        if dividend <= 0:
            raise UnhandledException(
                message="Impossible to calculate the PE ratio. "
                        "The Dividend yield value for '%s' is <= 0" %
                        stock.symbol)

        pe_ratio = stock.ticker_price / dividend

    return pe_ratio


def calculate_trades_stock_price(trades):
    """
    Calculate the Stock Price of the given stock trades
    :param trades:
    :return: the stock price
    """

    stock_price = 0.0
    trade_price_accum = 0.0
    share_quantity_accum = 0.0

    for trade in trades:
        trade_price_accum += trade.price * trade.shares_quantity
        share_quantity_accum += trade.shares_quantity

    if share_quantity_accum > 0.0:
        stock_price = trade_price_accum / share_quantity_accum

    return stock_price
