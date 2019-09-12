def iterPower(base, exp):
    if exp == 0:
        return 1

    result = base

    for i in range(1, exp):
        result = result * base

    return result


print(iterPower(10, 1))
