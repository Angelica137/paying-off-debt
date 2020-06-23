from scripts.minmonthpymt import MinMonthPymt


class Statement:
    def __init__(self, balance, minMonthPymtRate):
        self._balance = balance
        self._minMonthPymtRate = minMonthPymtRate
        self._minPmtThisMonth = 0

    def getMinPmt(self, balance, minMonthPymtRate):
        minPmtThisnMonth = MinMonthPymt(balance, minMonthPymtRate)
        return minPmtThisnMonth.calcMinMonPymt(minMonthPymtRate, balance)

    def printStatement(self, balance, minPmtThisMonth):
        return "Balance: " + str(balance) + "; Minimum Payment: " + str(minPmtThisMonth)
