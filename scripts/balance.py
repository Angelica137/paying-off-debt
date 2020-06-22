class Balance:
    def __init__(self, outsBalance, monthUnpaidBalance, monthRate):
        self._outsBalance = outsBalance
        self._monthUnpaidBalance = monthUnpaidBalance
        self._monthRate = monthRate

    def calcOutsBalance(self):
        self._outsBalance = self._monthUnpaidBalance + \
            (self._monthRate * self._monthUnpaidBalance)
        return round(self._outsBalance, 2)


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


class MonthlyIntRate:
    def __init__(self, intAnnual):
        self._intAnnual = intAnnual

    def calcMonthRate(self):
        return self._intAnnual / 12
