varA = "string"
varB = "another string"


if type(varA) == str and type(varB) == str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")
