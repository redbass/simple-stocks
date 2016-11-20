import csv

from stock_service import ROOT_PATH
from stock_service.model.stock import Stock

KEYS = ["symbol", "stock_type", "last_dividend", "fixed_dividend", "par_value"]

STOCKS_FILE = ROOT_PATH + "/resource/data.csv"


def load_base_stocks():
    """
    The function fead from a csv a list of stocks and returns the list of
    Stock object
    :return: stocks list
    :rtype Array of Stocks
    """

    stocks = {}

    with open(STOCKS_FILE) as d:
        data = csv.reader(d)

        for row in data:

            values = dict(zip(KEYS, row))
            _cast_values(values)
            stock = Stock(**values)

            stocks[stock.symbol] = stock

    return stocks


def _cast_values(values):
    values['last_dividend'] = float(values['last_dividend'] or 0.0)
    values['par_value'] = float(values['par_value'] or 0.0)
