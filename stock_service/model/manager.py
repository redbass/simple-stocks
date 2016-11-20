import copy
import logging

from stock_service.lib.data import load_base_stocks
from stock_service.lib.exceptions import StockNotFound
from stock_service.model.trade import Trade


class TradeManager(object):

    _instance = None
    _trades = []
    _stocks = {}

    def __init__(self):

        self._stocks = load_base_stocks()

        logging.info("Trade manager initialized with '%s' stock" %
                     len(self._stocks))

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

        prev_price = stock.ticker_price
        stock.ticker_price = trade.price
        logging.info("The ticker price for the stock '%s' has been set to %s "
                     "(before '%s')" % (stock.symbol, stock.ticker_price,
                                        prev_price))

    def has_stock(self, symbol):
        """
        Checks if the given simbol is stored in the manager

        :param symbol: Symbol string
        :rtype Boolean
        """
        return symbol in self._stocks

    def get_stocks(self):
        """
        Return the list of all the st
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




