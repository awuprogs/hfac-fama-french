import numpy as np
import transaction
from portfolio import Portfolio
from itertools import islice
import pandas as pd
import datetime as dt


if __name__ == '__main__':
    # read in transactions file and construct list of transactions
    transactions = []
    f = open('transactions.csv', 'rb')
    for line in islice(f, 1, None):
        transactions.append(transaction.Transaction(line))

    # flipe order of transactions, so most recent is last
    transactions.reverse()

    # turn transaction objects into portfolio objects
    portfolios = []
    init_cash = 10000 
    for t in transactions:
        if len(portfolios) == 0:
            portfolios.append(Portfolio(t, init_cash = init_cash))
        else:
            portfolios.append(Portfolio(t, portfolios[-1]))


    # get all trading days as a list
    bizdates = pd.bdate_range(portfolios[0].start_date, dt.date.today() - dt.timedelta(days=1))

    # get portfolio values
    portfolios_length = len(portfolios)
    idx = 0
    values = []
    for date in bizdates:
        if idx + 1 < portfolios_length and portfolios[idx + 1].start_date <= date.to_datetime():
            idx += 1
        values.append(portfolios[idx].calculateValue(date))
    print values
    
    # TODO: calculate returns and/or output them

    


