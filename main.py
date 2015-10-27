import numpy as np
import transaction
import csv
from itertools import islice

if __name__ == '__main__':
    # read in transactions file and construct list of transactions
    transactions = []
    f = open('transactions.csv', 'rb')
    for line in islice(f, 1, None):
        transactions.append(transaction.Transaction(line))

    # # construct portfolios
    # portfolios = []
    # for t in transactions:
    #     if len(portfolios = 0):
    #         portfolios.append(Portfolio(t))
    #     else:
    #         portfolios.append(Portfolio(t, portfolios[-1]))

    # # TODO: figure out format for dates and way to get all trading days
    # # get portfolio values
    # idx = 0
    # values = []
    # for date in dates:
    #     if portfolios[idx + 1].start_date <= date:
    #         idx += 1
    #     values.append(portfolios[idx].calculateValue(date))

    # TODO: calculate returns and/or output them

