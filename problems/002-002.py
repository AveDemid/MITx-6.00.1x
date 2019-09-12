balance = 3926
annualInterestRate = 0.2

guess = round(balance / 12, -1)

newBalance = balance

while newBalance >= 0:
    newBalance = balance
    for i in range(1, 13):
        newBalance = newBalance - guess
        newBalance = newBalance + newBalance * (annualInterestRate / 12)
    guess += 10


print("Lowest Payment:", int(guess - 10))
