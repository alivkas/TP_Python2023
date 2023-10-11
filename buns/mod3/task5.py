stringNums = input("Введите строку ")
list = ["yes" if stringNums.count("0") == stringNums.count("1") else "no"]
print(list[0])
