
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0
while month < 12:
    minMonthPmt = monthlyPaymentRate * balance
    monthUnpaidBal = balance - minMonthPmt
    newBal = monthUnpaidBal + (annualInterestRate/12)*monthUnpaidBal
    balance = round(newBal, 2)
    month += 1
print("Remaining balance: " + str(balance))
