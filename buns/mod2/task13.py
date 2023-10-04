code = input("Введите штрих код ")
even = 0
odd = 0

for odd_num in range(0, len(code), 2):
    odd += int(code[odd_num])

for even_num in range(1, len(code), 2):
    even += int(code[even_num]) * 3

if (even + odd) % 10 == 0:
    print("yes")
else:
    print("no")