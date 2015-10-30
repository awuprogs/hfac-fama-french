import numpy as np
from yahoo_finance import Share
import copy
import transaction


class Portfolio:
    """
    t = type Transaction
    TODO:
    Create new portfolio given old portfolio and a Transaction object. When
    last_portfolio is None, it means that our old portfolio was empty. Also,
    keep an instance variable start_date with the date of the transaction.
    """

    def __init__(self, t, last_portfolio=None, init_cash=None):

        # dictionary self.holdings: map from symbol (string) to qty (# shares)
        qty = t.direction * t.quantity
        if last_portfolio:
            self.holdings = copy.deepcopy(last_portfolio.holdings)
            if t.symbol in last_portfolio.holdings:
                self.holdings[t.symbol] += qty
            else:
                self.holdings[t.symbol] = qty
        else:
            self.holdings = {}
            self.holdings[t.symbol] = qty
            self.holdings['cash'] = init_cash

        self.holdings['cash'] -= (qty * t.price + t.comm)

        # start_date

        self.start_date = t.date

    """
    TODO:
    Given date, calculate the value of the portfolio. Try to verify that the
    date is after the start_date. Feel free to use packages 
    """

    def calculateValue(self, date):
        value = 0.
        date = date.strftime('%Y-%m-%d')
        for sym,qty in self.holdings.iteritems():
            if sym == "Cash":
                value += qty
            else:
                stock = Share(sym)
                close_price = float(stock.get_historical(date, date)[0]['Adj_Close'])
                value += close_price * qty

        return value

