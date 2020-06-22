from scripts.minmonthpymt import MinMonthPymt


class Statement:
    def __init__(self, balance, minMonthPymtRate):
        self._balance = balance
        self._minMonthPymtRate = minMonthPymtRate

    def getMinPymt(self, balance, minMonthPymtRate):
        minPymtThisnMonth = MinMonthPymt(balance, minMonthPymtRate)
        return minPymtThisnMonth.calcMinMonPymt(minMonthPymtRate, balance)
