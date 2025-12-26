a = 3
b = 5
c = 7
if a < b :
    print("a is less than b")
    print("a is less than b!")
    print("a is less than b!!")

if a < b and b < c :
    print("a is less than b and b is less than c")

if a < b or b < c :
    print("a is less than b or b is less than c")

if a > b :
    print("a is greater than b")
else :
    print("a is not greater than b")

#
if a > b :
    print("a is greater than b")
elif a < b :
    print("a is less than b")
else :
    print("a is equal to b")