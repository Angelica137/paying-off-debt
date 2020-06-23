from debtprojection import DebtProjection


class TwelveMonthProjection:
    def __init__(self, balance, minMonthPymtRate):
        self._balance = balance
        self._minMonthPymtRate = minMonthPymtRate
        self._minPmtThisMonth = 0
        self._unpaidBalance = 0
        self._annualInt = 0.2
        self._monthlyInt = 0

    def runProjection(self, balance, minMonthPymtRate, minPmtThisMonth, annualInt, unpaidBlalance):
        debtProjection = DebtProjection(balance, minMonthPymtRate)
        month = 0
        while month < 12:
            debtProjection.getMinMonPmt(balance, minMonthPymtRate)
            debtProjection.getMonUnpaidBalance(balance, minPmtThisMonth)
            monthlyInt = debtProjection.monthlyIntRate(annualInt)
            balance = debtProjection.getNextMonthBalance(
                unpaidBlalance, monthlyInt)
            month += 1
            print(round(balance, 2))
