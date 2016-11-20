Simple Stocks
=============

Simple stock is a service that provide some basic methods to print in console the result of some operations on GBCE stock trades.
 The methods supported are:
 - Calculate stock dividend yield (service.calculate_dividend_yield)
 - Calculate stock P/E ratio (calculate_pe_ratio)
 - Calculate stock price (calculate_stock_price)
 - Calculate share index (calculate_share_index)

The Stock Simple Service is using an instance of a trade manager that is initialized with these stocks:
    
|symbol| stock_type | last_dividend | fixed_dividend |par_value |
|------|------------|---------------|----------------|----------|
| TEA  |Common      |8              |                |100       |
| POP  |Common      |8              |                |100       |
| ALE  |Common      |23             |                |60        |
| GIN  |Preferred   |8              |2%              |100       |
| JOE  |Common      |13             |                |250       |


Tests
-----
In the Test folder are available few tests. 

    python -m unittest discover -s stock_service/test/ -p 'test_*'
    
Some dependencies are required

    pip install -r requirements.tests.txt


Examples
--------
Is possible to run a example script that is showing how to use the service

    python stock_service/example.py
    
