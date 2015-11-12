import numpy as np
import transaction
from portfolio import Portfolio
from itertools import islice
import pandas as pd
import datetime as dt
import csv 

# i have no idea what happened to this day
# 6/17/14   11736307758 Sold 975 @ 0.65 975     0.65        633.75  --- 

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
    print bizdates

    # storage for prices from yahoo finance
    prices = {}
    # get portfolio values
    portfolios_length = len(portfolios)
    idx = 0
    values = []
    for date in bizdates:
        if idx + 1 < portfolios_length and portfolios[idx + 1].start_date <= date.to_datetime():
            idx += 1
        (value, new_prices) = portfolios[idx].calculateValue(date, prices)
        # if portfolio doesn't exist on that day, remove date from bizdates
        if (value, new_prices) != (None, None):
            values.append(value)
            prices = new_prices
        else: 
            bizdates.drop(date)
    print values
    
    # stringify dates
    string_dates = [date.to_datetime().strftime('%Y-%m-%d') for date in bizdates]

    # export to CSV file
    my_csv = open('values.csv', 'w')
    data = zip(string_dates, values)
    a = csv.writer(my_csv)
    a.writerows(data)
    my_csv.close()


