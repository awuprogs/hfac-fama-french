import numpy as np
import transaction
from portfolio import Portfolio
from itertools import islice
import pandas as pd
import datetime as dt
import csv 
import copy

# if qty of any stock is negative (check in calculate value function) throw error

if __name__ == '__main__':
    # read in transactions file and construct list of transactions
    transactions = []
    f = open('real_transactions.csv', 'rb')
    for line in islice(f, 1, None):
        transactions.append(transaction.Transaction(line))

    # flipe order of transactions, so most recent is last
    transactions.reverse()

    # turn transaction objects into portfolio objects
    portfolios = []
    init_cash = 30000 
    for t in transactions:
        if len(portfolios) == 0:
            portfolios.append(Portfolio(t, init_cash = init_cash))
        else:
            portfolios.append(Portfolio(t, portfolios[-1]))


    # get all trading days as a list
    bizdates = pd.bdate_range(portfolios[0].start_date, dt.date.today() - dt.timedelta(days=1))

    # storage for prices from yahoo finance
    prices = {}
    # get portfolio values
    portfolios_length = len(portfolios)

    idx = 0
    values = []
    cpy_bizdates = copy.deepcopy(bizdates)
    for date in bizdates:
        print date
        if idx + 1 < portfolios_length and portfolios[idx + 1].start_date <= date.to_datetime():
            idx += 1
        
        (value, new_prices) = portfolios[idx].calculateValue(date, prices)
        # if portfolio doesn't exist on that day, remove date from bizdates
        if (value, new_prices) != (None, None):
            values.append(value)
            prices = new_prices
        else: 
            cpy_bizdates = cpy_bizdates.drop(date)
    print len(values)
    print len(cpy_bizdates)
    
    # stringify dates
    string_dates = [date.to_datetime().strftime('%Y-%m-%d') for date in cpy_bizdates]

    # export to CSV file
    my_csv = open('values.csv', 'w')
    data = zip(string_dates, values)
    a = csv.writer(my_csv)
    a.writerows(data)
    my_csv.close()


