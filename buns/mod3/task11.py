field = []
k = int(input("Введите размерность поля "))
for i in range(k):
    row = input().strip()
    field.append(row)


def check_winner(symbol):
    for row in field:
        if row.count(symbol) == k:
            return symbol

    for j in range(k):
        col = [row[j] for row in field]
        if col.count(symbol) == k:
            return symbol

    diag1 = [field[i][i] for i in range(k)]
    if diag1.count(symbol) == k:
        return symbol

    diag2 = [field[i][k-i-1] for i in range(k)]
    if diag2.count(symbol) == k:
        return symbol

    return None


x_winner = check_winner("X")
if x_winner:
    print("X")
else:
    o_winner = check_winner("O")
    if o_winner:
        print("O")
    else:
        print("Ничья")