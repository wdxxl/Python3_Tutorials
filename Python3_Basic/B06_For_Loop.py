# Python for loop
# English http://www.w3resource.com/python/python-for-loop.php
# For in list
color_list = ["Red","Blue","Green","Black"]
for c in color_list:
    print(c,end="|")
print()

# For in range
for a in range(4):
    print(a,end="|")
print()

for a in range(2,7):
    print(a,end="|")
print()

for a in range(2,19,5):
    print(a,end="|")
print()

# Iterating over tuple
print("# Iterating over tuple")
numbers = (1,2,3,4,5,6,7,8,9)   # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
    if x % 2:
        count_odd+=1
    else:
        count_even+=1
print("Number of even numbers :", count_even)
print("Number of odd numbers :", count_odd)
print()

# Iterating over list
print("# Iterating over list")
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0,1), [5,12], {"class":"V", "Section":'A'}]
for item in datalist:
    print("Type of", item, "is", type(item))
print()

# Iterating over dictionary
print("# Iterating over dictionary")
color = {"c1":"Red", "c2":"Green", "c3": "Orange"}
for key in color:
    print(key, end="|")
print()
for value in color.values():
    print(value, end="|")
print()
for key in color:
    print(key +":"+ color[key], end="|")
print()
