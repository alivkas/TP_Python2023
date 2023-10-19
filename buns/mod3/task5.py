string_nums = input("Введите строку ")
list = ["yes" if string_nums.count("0") == string_nums.count("1") else "no"]
print(list[0])
