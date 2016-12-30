
for letter in 'Python':
    if letter == 'h': continue
    print(letter, end="|")
print()

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print(var, end="|")
print()
print("Good Bye!")
