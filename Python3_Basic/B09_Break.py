
for letter in 'Python':
    if letter == 'h': break
    print(letter, end="|")
print()

var = 10
while var > 0:
    print(var, end="|")
    var -= 1
    if var == 5:
        break
print()
print("Good Bye!")
