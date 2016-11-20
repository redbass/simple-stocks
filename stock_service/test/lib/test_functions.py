from mock import patch

from unittest import TestCase

from stock_service.lib.functions import calculate_dividend_yield, NULL_VALUE, \
    calculate_pe_ratio, calculate_trades_stock_price
from stock_service.model.stock import Stock, StockType
from stock_service.model.trade import Trade, TradeType


TEST_TRADES = [
        Trade("TEA", TradeType.SELL, 20, 12.23),
        Trade("POP", TradeType.BUY, 80, 7.56),
        Trade("TEA", TradeType.BUY, 450, 10.20),
        Trade("POP", TradeType.SELL, 50, 6.20),
        Trade("ALE", TradeType.SELL, 214, 25.67)
    ]


class TestFunctions(TestCase):

    def test_calculate_dividend_yield_COMMON(self):
        # Given a generic stock
        last_dividend = 8
        stock = Stock("TST", StockType.COMMON, last_dividend, "", 100)

        # And I'm setting a ticker_price grater then 0
        stock.ticker_price = 1

        # When i'm calling the function calculate_dividend_yield
        dividend_yield = calculate_dividend_yield(stock)

        # Then then the dividend_yield have to be:
        #  dividend_yield / stock.ticker_price
        expected_value = dividend_yield / stock.ticker_price
        self.assertEquals(expected_value, last_dividend)

    def test_calculate_dividend_yield_other_stock_type(self):
        # Given a generic stock
        last_dividend = 8
        fixed_dividend = 0.02
        par_value = 100
        str_fixed_dividend = str(fixed_dividend * 100) + "%"

        stock = Stock("TST", StockType.PREFERRED, last_dividend,
                      str_fixed_dividend, par_value)

        # And I'm setting a ticker_price grater then 0
        stock.ticker_price = 1

        # When i'm calling the function calculate_dividend_yield
        dividend_yield = calculate_dividend_yield(stock)

        # Then then the dividend_yield have to be:
        #  fixed_dividend * par_value / stock.ticker_price
        expected_value = fixed_dividend * par_value / stock.ticker_price
        self.assertEquals(expected_value, dividend_yield)

    def test_calculate_dividend_yield_0_ticker_price(self):
        # Given a generic stock
        last_dividend = 8
        stock = Stock("TST", StockType.COMMON, last_dividend, "", 100)

        # When the stock.ticker_price is 0
        self.assertEquals(stock.ticker_price, 0)
        # And I'm calling the function
        dividend_yield = calculate_dividend_yield(stock)

        # Then the expected value is -1.0
        self.assertEquals(dividend_yield, NULL_VALUE)

    @patch("stock_service.lib.functions.calculate_dividend_yield")
    def test_calculate_pe_ratio(self, c_dividend_yield):
        # Given a generic stock
        last_dividend = 8
        stock = Stock("TST", StockType.COMMON, last_dividend, "", 100)

        # And I'm setting a ticker_price grater then 0
        stock.ticker_price = 1

        # And calculate_dividend_yield is mock
        c_dividend_yield.return_value = last_dividend

        # When I'm calling the function calculate_pe_ratio
        pe_ratio = calculate_pe_ratio(stock)

        # Then the result have to be
        self.assertEquals(stock.ticker_price / last_dividend, pe_ratio)

        # And that calculate_dividend_yield has been called once
        c_dividend_yield.assert_called_once()

    def test_calculate_pe_ratio_0_ticker_price(self):
        # Given a generic stock
        last_dividend = 8
        stock = Stock("TST", StockType.COMMON, last_dividend, "", 100)

        # When the stock.ticker_price is 0
        self.assertEquals(stock.ticker_price, 0)
        # And I'm calling the function
        dividend_yield = calculate_dividend_yield(stock)

        # Then the expected value is -1.0
        self.assertEquals(dividend_yield, NULL_VALUE)

    def test_calculate_trades_stock_price(self):
        # Given a list of trades
        trades = TEST_TRADES[:]

        # When I'm calling calculate_trades_stock_price
        stock_price = calculate_trades_stock_price(trades)

        # Then the stock price have to be
        self.assertEquals(stock_price, 13.81176904176904)

    def test_calculate_trades_stock_price_shares_quantity_0(self):
        # Given a list of trades
        trades = TEST_TRADES[:]
        # And all the shares_quantity are 0
        for trade in trades:
            trade.shares_quantity = 0

        # When I'm calling calculate_trades_stock_price
        stock_price = calculate_trades_stock_price(trades)

        # Then the stock price have to be
        self.assertEquals(stock_price, 0.0)

    def test_calculate_trades_stock_price_no_trades(self):
        # Given a empty list of trades
        trades = []

        # When I'm calling calculate_trades_stock_price
        stock_price = calculate_trades_stock_price(trades)

        # Then the stock price have to be
        self.assertEquals(stock_price, 0.0)
