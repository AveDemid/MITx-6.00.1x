string = "abcdefghklmnop"


def isIn(char, aStr):
    if(len(aStr) == 0):
        return False

    middle = int(len(aStr) / 2)

    if(char == aStr[middle]):
        return True

    if(len(aStr) <= 1):
        return False

    if(char > aStr[middle]):
        return isIn(char, aStr[middle:])
    if(char < aStr[middle]):
        return isIn(char, aStr[0:middle])


print(isIn("z", string))
