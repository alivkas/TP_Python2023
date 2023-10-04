numbers = input("Введите три числа в формате (a b c) ")

space = 0
len_a = 0
len_b = 0

for sym in numbers:
    if sym == " ":
        space += 1
    if space == 0:
        len_a += 1
    elif space == 1:
        len_b += 1

a = int(numbers[0:len_a:])
b = int(numbers[len_a + 1:len_a + len_b:])
c = int(numbers[len_a + len_b + 1:])

if a > b:
    a, b = b, a

if b > c:
    b, c = c, b

if a > b:
    a, b = b, a

print(b)