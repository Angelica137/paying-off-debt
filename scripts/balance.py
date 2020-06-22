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


"""
class MonthlyInt:
    def __int__(self, intAnnual):
        self._intAnnual = intAnnual

    def intMonth(self):
        intMonth = self._intAnnual / 12
"""
