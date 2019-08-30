# First
for i in range(2, 11, 2):
    print(i)
print("Goodbye!")

# Second
print("Hello!")
for i in range(10, 1, -2):
    print(i)

# third
end = 6
total = 0
for i in range(1, end + 1):
    total += i
print(total)


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
