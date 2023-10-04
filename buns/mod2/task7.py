string = input("Введите строку из нулей и единиц ")
units = 0
zero = 0

for num in string:
    if num == "1":
        units += 1
    if num == "0":
        zero += 1

if units == zero:
    print("yes")
else:
    print("no")