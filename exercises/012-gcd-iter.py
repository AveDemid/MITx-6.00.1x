def gcdIter(a, b):
    gcd = 0

    if(a > b):
        gcd = a
    else:
        gcd = b

    while a % gcd != 0 or b % gcd != 0 or gcd == 1:
        print(gcd, "PRIIINT")

        gcd = gcd - 1

    return gcd


print(10 % 20)
