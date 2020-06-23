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
            formatBalance = round(balance, 2)
            month += 1
            print("Month " + str(month) +
                  " Remaining balance: " + str(formatBalance))
            print("Remaining balance: " + str(formatBalance))


balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
p = TwelveMonthProjection(42, 0.04)
print(p.runProjection(42, 0.04, 1.68, 0.2, 40.32))
