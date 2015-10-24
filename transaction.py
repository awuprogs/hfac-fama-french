import numpy as np

class Transaction:
    """
    TODOs:
    (1) Feel free to use whatever types you want 
    (2) Specify these in these comments
    """
    def __init__(self,
                 date,
                 direction,
                 symbol,
                 quantity,
                 price,
                 comm):
        self.date      = date
        self.direction = direction
        self.symbol    = symbol
        self.quantity  = quantity
        self.price     = price
        self.comm      = comm

    """
    TODO: Convert line (string) to a transaction object. Calls __init__ above
    with appropriate parameters.

    Hint: The 'split' function might be useful.
    """
    def __init__(self, line):
        pass

