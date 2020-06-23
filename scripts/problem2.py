balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
outsBalance = balance
while outsBalance > 0:
    monthlyPayment += 10
    outsBalance = balance
    month = 1

    while month <= 12 and outsBalance > 0:
        monthUnpaidBalance = outsBalance - monthlyPayment
        updatedBalance = monthUnpaidBalance + \
            (monthlyInterestRate * monthUnpaidBalance)
        outsBalance = updatedBalance
        month += 1
    outsBalance = round(outsBalance)

print("Lowest Payment: " + str(monthlyPayment))
