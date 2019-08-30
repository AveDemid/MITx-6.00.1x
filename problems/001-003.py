s = 'vwmfkxdz'

temp = ""
total = ""

# TODO refactoring this shit :|
for i in range(len(s)-1):
    if len(temp) == 0:
        temp = s[i]
    if temp[-1] <= s[i+1]:
        temp += s[i+1]
        if temp == s:
            total = temp
        if len(s) == i + 2 and len(temp) > len(total):
            total = temp
    else:
        if len(temp) > len(total):
            total = temp
        temp = ""


print("Longest substring in alphabetical order is:", total)
