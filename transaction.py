import numpy as np
import datetime
from dateutil import parser


class Transaction:
    """
    TODOs:
    (1) Feel free to use whatever types you want 
    (2) Specify these in these comments
    """
    def my_init(self,
                date,
                direction,
                symbol,
                quantity,
                price,
                comm):
        # datetime.date
        self.date      = date
        # boolean, True = Buy, False = Sell
        self.direction = direction
        # string
        self.symbol    = symbol
        # int
        self.quantity  = quantity
        # float 
        self.price     = price
        # float
        self.comm      = comm
    
    """
    TODO: Convert line (string) to a transaction object. Calls __init__ above
    with appropriate parameters.

    Hint: The 'split' function might be useful.
    """

    def __init__(self, line):
        info_arr = line.split(',')
        date = parser.parse(info_arr[0])
        if (info_arr[2][0] == 'B'):
            direction = True
        else:
            direction = False
        quantity = int(info_arr[3])
        symbol = info_arr[4]
        price = float(info_arr[5])
        comm = float(info_arr[6])
        self.my_init(date, direction, symbol, quantity, price, comm)
        # print "self.price " + str(self.price)
        # print "self.date " + str(self.date)
        # print "self.symbol" + self.symbol


