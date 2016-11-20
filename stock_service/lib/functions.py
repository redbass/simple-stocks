from datetime import datetime

from stock_service.model.stock import StockType


def calculate_dividend_yield(self):
    """
    Calculate the dividend yieald
    :return: dividend yield
    :rtype float
    """
    dividend_yield = -1.0

    if self.ticker_price > 0.0:
        if self.stock_type == StockType.COMMON:
            dividend_yield = self.last_dividend / self.ticker_price
        else:
            dividend_yield = \
                self.fixed_dividend * self.par_value / self.ticker_price

    return dividend_yield


def get_trades_in_range(trades, stock_symbol, period_min=15):
    """
    Return a generator of trades inputted in the last 'period_min' minutes
    :param stock_symbol
    :param period_min: minutes
    :rtype: generator of trades
    """

    # if not self.has_stock(stock_symbol):
    #     raise StockNotFound(stock_symbol)

    end_period = datetime.utcnow()
    start_period = end_period - datetime.timedelta(minutes=period_min)

    return [trade for trade in trades
            if (start_period < trade.timeStamp <= end_period or
                period_min == 0) and
            trade.stock_symbol == stock_symbol]


def calculate_trades_stock_price(trades):
    """

    :param trades:
    :return:
    """

    # trades = self.get_trades_in_range(stock_symbol, period)

    stock_price = 0.0
    trade_price_accum = 0.0
    share_quantity_accum = 0.0

    for trade in trades:
        trade_price_accum += trade.price * trade.shares_quantity
        share_quantity_accum += trade.shares_quantity

    if share_quantity_accum > 0.0:
        stock_price = trade_price_accum / share_quantity_accum

    return stock_price
