numbers = input("Введите два числа в формате (a, b) ")
slicer = 0

for sym in numbers:
    if sym != ",":
        slicer += 1
    else:
        break

a = int(numbers[0:slicer:])
b = int(numbers[slicer + 2:])

print(a % b)
