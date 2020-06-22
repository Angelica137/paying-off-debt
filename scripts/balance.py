class Balance:
    def __init__(self, outsBalance, monthUnpaidBalance, monthRate):
        self._outsBalance = outsBalance
        self._monthUnpaidBalance = monthUnpaidBalance
        self._monthRate = monthRate

    def calcOutsBalance(self):
        self._outsBalance = self._monthUnpaidBalance + \
            (self._monthRate * self._monthUnpaidBalance)
        return round(self._outsBalance, 2)
