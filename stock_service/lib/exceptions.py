
class StockNotFound(Exception):
    def __init__(self, symbol, *args, **kwargs):
        message = "Stock '%s' not found" % symbol
        super(StockNotFound, self).__init__(message, *args, **kwargs)


class UnhandledException(Exception):
    def __init__(self, message, *args, **kwargs):
        super(UnhandledException, self).__init__(message,
                                                 *args, **kwargs)
