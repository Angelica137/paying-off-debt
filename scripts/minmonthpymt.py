class MinMonthPymt:
    def __init__(self, minMonthPymtRate, balance):
        self._minMonthPymtRate = minMonthPymtRate
        self._balance = balance

    def calcMinMonPymt(self, minMonthPymtRate, balance):
        return self._minMonthPymtRate * self._balance
