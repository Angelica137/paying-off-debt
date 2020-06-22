class MonthlyIntRate:
    def __init__(self, intAnnual):
        self._intAnnual = intAnnual

    def calcMonthRate(self):
        return self._intAnnual / 12
