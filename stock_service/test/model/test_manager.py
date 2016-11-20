from unittest import TestCase

from datetime import timedelta

from stock_service.model.manager import TradeManager
from stock_service.model.trade import Trade
from stock_service.model.trade import TradeType


class TestManager(TestCase):

    def test_TradeManager_init(self):
        # Given a TradeManager
        manager = TradeManager()

        # Then the manager have in memory 5 stocks
        self.assertEquals(len(manager._stocks), 5)

    def test_record_trade(self):
        # Given a TradeManager
        manager = TradeManager()
        # And there are no trades stored
        trades = manager.get_trades()
        self.assertEquals(len(manager.get_trades()), 0)

        # When I record a trade
        trade = Trade("TEA", TradeType.SELL, 22, 21.23)
        manager.record_trade(trade)

        # Then a new trade is in the manager
        trades = manager.get_trades()
        self.assertEquals(len(trades), 1)

    def test_get_trades_in_range(self):
        stock_symbol = "TEA"
        period = 15

        # Given a TradeManager
        manager = TradeManager()

        # And some trades are stored
        trade1 = Trade(stock_symbol, TradeType.SELL, 22, 21.23)
        manager.record_trade(trade1)
        trade2 = Trade(stock_symbol, TradeType.SELL, 20, 20.23)
        manager.record_trade(trade2)
        trade3 = Trade("ALE", TradeType.SELL, 22, 21.23)
        manager.record_trade(trade3)

        # And one has been recorded few minutes before period value
        trade2.timeStamp = trade2.timeStamp - timedelta(minutes=period + 10)

        # When I call get_trades_in_range
        trades = manager.get_trades_in_range(stock_symbol, period)

        # Then the result is one element
        self.assertEquals(len(trades), 1)

        # And trade1 is the ony one in the list
        self.assertIn(trade1, trades)
        self.assertNotIn(trade2, trades)
        self.assertNotIn(trade3, trades)
