
balance = 411899
annualInterestRate = 0.15

monthlyInterestRate = annualInterestRate/12
outsBalance = balance
lowerBound = outsBalance/12
upperBound = (outsBalance * (1 + monthlyInterestRate)**12) / 12
"""
the absolute value of outsBlanace must be used to account for negative
balances. You want your final balance to be 0, not +/-
0.01 is the value of epsilon
You cannot use zero because using this methos we are just approximating a value
and using zero will lead to an infinite loop
"""
while abs(outsBalance) > 0.01:
    monthlyPayment = (upperBound + lowerBound) / 2
    outsBalance = balance
    month = 0
    while month < 12:
        """
         here you calculate the outstanding balance after making a payment
         using mid point
         """
        monthUnpaidBalance = outsBalance - monthlyPayment
        updatedBalance = monthUnpaidBalance + \
            (monthlyInterestRate * monthUnpaidBalance)
        outsBalance = updatedBalance
        month += 1
        """
        then, you check if the resulting balance is too low or too high
        and recalculate the mid point if needed.
        """
    if outsBalance > 0.01:
        lowerBound = monthlyPayment
    elif outsBalance < 0.01:
        upperBound = monthlyPayment
    else:
        break

formatMonthlyPmt = round(monthlyPayment, 2)
print("Lowest Payment: " + str(formatMonthlyPmt))
