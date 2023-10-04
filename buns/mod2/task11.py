numbers = input("Введите цифры через пробел ")
flag = False

for num1 in range(0, len(numbers), 2):
    for num2 in range(0, len(numbers), 2):
        if numbers[num1] == numbers[num2 + 2]:
            print(True)
            flag = True
            break
        else:
            print(False)
            flag = True
            break
    if flag:
        break