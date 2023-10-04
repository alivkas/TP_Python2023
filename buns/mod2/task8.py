input_string = input("Введите строку и символ в формате ('xyyxyxx,x') ")

count = 0
slicer = 0

for element in input_string:
    if element != ",":
        slicer += 1
    else:
        break

string = input_string[0:slicer:]
sym = input_string[slicer + 1:]

for symbol in string:
    if symbol == sym:
        count += 1
    else:
        break

print(count)

