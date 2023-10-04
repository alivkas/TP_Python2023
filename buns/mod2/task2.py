side = float(input("Введите сторону квадрата "))

perimeter = side * 4
square = side ** 2
diagonal = round((side ** 2 + side ** 2) ** 0.5, 2)

print('%.2f' % perimeter, '%.2f' % square, diagonal, sep=", ")
