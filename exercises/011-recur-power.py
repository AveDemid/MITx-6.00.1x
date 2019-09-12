def recurPower(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)


print(recurPower(10, 0))
