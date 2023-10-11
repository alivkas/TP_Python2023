words = input("Введите слова через пробел ").split()
list = [x[-1] for x in words]
print("".join(list))