num = int(input("Введите число "))
print("Неверный ввод" if num < 1 else ", ".join([bin(num)[2:], oct(num)[2:], hex(num)[2:]]))