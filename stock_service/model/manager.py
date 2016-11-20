import copy
from datetime import datetime
from datetime import timedelta

from stock_service.lib.data import load_base_stocks
from stock_service.lib.exceptions import StockNotFound
from stock_service.model.trade import Trade


class TradeManager(object):

    def __init__(self):
        self._stocks = load_base_stocks()
        self._trades = []

    def record_trade(self, trade):
        """
        Add a new trade to the trade manager
        :param trade:
        :type trade Trade
        :return:
        """

        if not isinstance(trade, Trade):
            raise ValueError(
                "The 'trade' parameter is not a valid 'Trade' object")

        stock = self.get_stock(trade.stock_symbol)
        self._trades.append(trade)
        stock.ticker_price = trade.price

    def has_stock(self, symbol):
        """
        Checks if the given simbol is stored in the manager

        :param symbol: Symbol string
        :rtype Boolean
        """
        return symbol in self._stocks

    def get_trades(self):
        """
        Return the list of all the trades
        :return: stock_service.model.trade.Trade
        """
        return copy.deepcopy(self._trades)

    def get_stocks(self):
        """
        Return the list of all the stocks
        :return: stock_service.model.stock.Stock
        """
        return copy.deepcopy(self._stocks).iteritems()

    def get_stock(self, symbol):
        """
        Return a stock 'symbol' object
        :param symbol: Stock symbol String
        :rtype
        """
        if not self.has_stock(symbol):
            raise StockNotFound(symbol)

        return self._stocks.get(symbol)

    def get_trades_by_symbol(self, stock_symbol):
        """
        Get a list of trades by symbol
        :param stock_symbol:
        :return:
        """
        self.get_trades_in_range(stock_symbol, 0)

    def get_trades_in_range(self, stock_symbol, period_min=15):
        """
        Return a generator of trades inputted in the last 'period_min' minutes
        :param stock_symbol
        :param period_min: minutes
        :rtype: generator of trades
        """

        if not self.has_stock(stock_symbol):
            raise StockNotFound(stock_symbol)

        end_period = datetime.utcnow()
        start_period = end_period - timedelta(minutes=period_min)

        return [trade for trade in self._trades
                if (start_period < trade.timeStamp <= end_period or
                    period_min == 0) and
                trade.stock_symbol == stock_symbol]


