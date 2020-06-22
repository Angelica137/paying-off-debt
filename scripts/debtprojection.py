from minmonthpymt import MinMonthPymt
from monthintrate import MonthlyIntRate


class DebtProjection:
    def __init__(self, balance, minMonthPymtRate):
        self._balance = balance
        self._minMonthPymtRate = minMonthPymtRate
        self._minPmtThisMonth = 0
        self._unpaidBalance = 0
        self._annualInt = 0.2
        self._monthlyInt = 0

    def getMinMonPmt(self, balance, minMonthPymtRate):
        minPmt = MinMonthPymt(balance, minMonthPymtRate)
        self._minPmtThisMonth = minPmt.calcMinMonPymt(
            minMonthPymtRate, balance)
        return self._minPmtThisMonth

    def getMonUnpaidBalance(self, balance, minPmtThisMonth):
        self._unpaidBalance = self._balance - self._minPmtThisMonth
        return self._unpaidBalance

    def monthlyIntRate(self, annualInt):
        monthlyInt = MonthlyIntRate(annualInt)
        self._monthlyInt = monthlyInt.calcMonthRate()
        return monthlyInt

    def getNextMonthBalance(self, unpaidBlalance, monthlyInt):
        self._balance = self._unpaidBalance + \
            (self._monthlyInt * self._unpaidBalance)
        return round(self._balance, 2)

    def twelveMonthProjection(self, unpaidBlalance, monthlyInt):
        month = 0
        while month < 12:
            self._balance = self._unpaidBalance + \
                (self._monthlyInt * self._unpaidBalance)
            month += 1
            print("hello")
            # return round(self._balance, 2)


projection1 = DebtProjection(42, 0.04)
print(projection1._balance)
projection1.getMinMonPmt(42, 0.04)
projection1.getMonUnpaidBalance(42, 1.68)
projection1._unpaidBalance
projection1.monthlyIntRate(0.2)

print(projection1.twelveMonthProjection(40.32, 0.2/12))
