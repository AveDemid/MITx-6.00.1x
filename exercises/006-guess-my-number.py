min = 0
max = 100
avarage = int((min + max) / 2)
isGuessed = False

greeteing = "Please think of a number between 0 and 100!"
rules = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."


print(greeteing)

while not isGuessed:
    print("Is your secret number" + " " + str(avarage) + "?")
    userResponse = input(rules)
    if(userResponse == "c"):
        isGuessed = True
    elif(userResponse == "l"):
        min = avarage
        avarage = int((min + max) / 2)
    elif(userResponse == "h"):
        max = avarage
        avarage = int((min + max) / 2)
    else:
        print("Sorry, I did not understand your input")

print("Game over. Your secret number was:", avarage)
