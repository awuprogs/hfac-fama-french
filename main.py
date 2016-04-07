import numpy as np
import transaction
from portfolio import Portfolio
import pandas as pd
import datetime as dt
import csv 
import copy

# if qty of any stock is negative (check in calculate value function) throw error

if __name__ == '__main__':
    # read in transactions file and construct list of transactions
    transactions = []
    f = open('transactions_clean_2.csv', 'r')
    lines = f.readlines()
    for line in lines:
        transactions.append(transaction.Transaction(line))

    # turn transaction objects into portfolio objects
    portfolios = [] # list of portfolio objects for each date
    init_cash = 6000 
    for t in transactions:
        if len(portfolios) == 0:
            portfolios.append(Portfolio(t, init_cash = init_cash))
        else:
            portfolios.append(Portfolio(t, portfolios[-1]))


    # get all trading days as a list
    bizdates = pd.bdate_range(portfolios[0].start_date, dt.date.today() - dt.timedelta(days=1))
    print(bizdates)
    # storage for prices from yahoo finance
    prices = {}

    # get portfolio values
    portfolios_length = len(portfolios)
    idx = 0
    values = {}
    cpy_bizdates = copy.deepcopy(bizdates)
    for date in bizdates:
        # advance to next portfolio on dates with transactions
        if idx + 1 < portfolios_length and portfolios[idx + 1].start_date <= date.to_datetime():
            idx += 1
        (value, new_prices) = portfolios[idx].calculateValue(date, prices)
        if (value, new_prices) != (None, None):
            values[date.to_datetime().strftime('%Y-%m-%d')] = value
            prices = new_prices
        # if portfolio doesn't exist on that day, remove date from bizdates
        else: 
            cpy_bizdates = cpy_bizdates.drop(date)
    print('Number of values:', len(values))
    print('Number of dates:', len(cpy_bizdates))
    print('Current holdings:')
    final_portfolio = portfolios[portfolios_length-1]
    for sym,shares in final_portfolio.holdings.items():
        print('Symbol:',sym,'Number of shares:',shares)

    # stringify dates
    string_dates = [date.to_datetime().strftime('%Y-%m-%d') for date in cpy_bizdates]

    # export to CSV file
    my_csv = open('values.csv','w',newline='\n')
    #valuelist = {value for date,value in sorted(values).items()}
    #data = zip(string_dates, valuelist)
    a = csv.writer(my_csv)
    for date,value in values.items():
        a.writerow([date,value])
    my_csv.close()


