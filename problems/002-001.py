balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


for i in range(1, 13):
    unpaidBalance = balance - balance * monthlyPaymentRate
    balance = unpaidBalance + annualInterestRate / 12 * unpaidBalance

print("Remaining balance:", round(balance, 2))
