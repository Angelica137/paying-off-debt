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


class DebtProjection:
    def __init__(self, balance, minMonthPymtRate):
        self._balance = balance
        self._minMonthPymtRate = minMonthPymtRate
        self._minPmtThisMonth = 0

    def getMinMonPmt(self, balance, minMonthPymtRate):
        minPmtThisnMonth = MinMonthPymt(balance, minMonthPymtRate)
        self._minPmtThisMonth = minPmtThisnMonth.calcMinMonPymt(
            minMonthPymtRate, balance)
        return self._minPmtThisMonth

    def getMonUnpaidBalance(self, balance, minPmtThisMonth):
        return self._balance - self._minPmtThisMonth

    # def getNextMonthBalance():
