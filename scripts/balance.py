class Balance:
    def __init__(self, outsBalance):
        self._outsBalance = outsBalance


"""
    def calcOutsBalance(self):
        self._outsBalance = MUP + MIR*MUP

    def getOutsBalance(self):
        return self._outsBalance
"""


class MinMonthPymt:
    def __init__(self, minMonthPymtRate, balance):
        self._minMonthPymtRate = minMonthPymtRate
        self._balance = balance

    def calcMinMonPymt(self, minMonthPymtRate, balance):
        return self._minMonthPymtRate * self._balance


class MonthUnpaidBalance:
    def __init__(self, balance, minMonthPymt):
        self._balance = balance
        self._minMonthPymt = minMonthPymt

    def calcMonthUnpaidBalance(self, balance, minMonthPymt):
        return self._balance - self._minMonthPymt


class MonthlyInt:
    def __init__(self, intAnnual):
        self._intAnnual = intAnnual

    def calcIntMonth(self):
        return self._intAnnual / 12
