size = int(input("Введите размерность квадратной матрицы: "))
matrix = [[i for i in range(1,size+1)] for j in range(0,size*size,size)]
print("Исходная матрица:")
for row in matrix:
    print(*row, sep=", ")

for i in range(size):
    for j in range(i+1,size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print("Транспонированная матрица:")
for row in matrix:
    print(*row, sep=", ")