from aetypes import Enum

from stock_service.lib.exceptions import UnhandledException


class StockType(Enum):
    # Common Stock: the dividend yield is calculated with last dividend.
    COMMON = "Common"

    # Preferred Stock: the dividend yield is calculated with fixed dividend.
    PREFERRED = "Preferred"


class Stock(object):

    def __init__(self, symbol, stock_type, last_dividend, fixed_dividend,
                 par_value):
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.ticker_price = 0.0

        if "%" in fixed_dividend:
            value = fixed_dividend[:-1].replace(" ", "")
            self.fixed_dividend = float(value) / 100

    def get_pe_ratio(self):
        pe_ratio = -1.0

        if self.ticker_price > 0.0:
            dividend = self.get_dividend_yield()

            if dividend <= 0:
                raise UnhandledException(
                    message="Impossible to calculate the PE ratio. "
                            "The Dividend yield value for '%s' is <= 0" %
                            self.symbol)

            pe_ratio = self.ticker_price / dividend

        return pe_ratio

