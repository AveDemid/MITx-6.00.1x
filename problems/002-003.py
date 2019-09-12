balance = 999999
annualInterestRate = 0.18

orig_balance = balance
monthlyInterest = annualInterestRate / 12
unpaidBalance = 0
lowerBound = balance / 12
upperBound = (balance + balance * annualInterestRate) / 12.0
epsilon = 0.01

while abs(balance) > epsilon:
    minPayment = (upperBound + lowerBound) / 2
    balance = orig_balance

    for i in range(12):
        unpaidBalance = balance - minPayment
        interest = monthlyInterest * unpaidBalance
        balance = unpaidBalance + interest

    if balance > epsilon:
        lowerBound = minPayment
    elif balance < epsilon:
        upperBound = minPayment
    else:
        break

print("Lowest Payment: ", round(minPayment, 2))
