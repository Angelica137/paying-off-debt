class MonthUnpaidBalance:
    def __init__(self, balance, minMonthPymt):
        self._balance = balance
        self._minMonthPymt = minMonthPymt

    def calcMonthUnpaidBalance(self, balance, minMonthPymt):
        return self._balance - self._minMonthPymt
