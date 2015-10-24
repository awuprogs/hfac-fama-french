import numpy as np

if __name__ == '__main__':
    # read in transactions file and construct list of transactions
    f = open('transactions.csv', 'wb')
    transactions = []
    for line in f:
        transactions.append(Transaction(line))

    # construct portfolios
    portfolios = []
    for t in transactions:
        if len(portfolios = 0):
            portfolios.append(Portfolio(t))
        else:
            portfolios.append(Portfolio(t, portfolios[-1]))

    # TODO: figure out format for dates and way to get all trading days
    # get portfolio values
    idx = 0
    values = []
    for date in dates:
        if portfolios[idx + 1].start_date <= date:
            idx += 1
        values.append(portfolios[idx].calculateValue(date))

    # TODO: calculate returns and/or output them

