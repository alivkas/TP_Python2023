number = int(input("Введите число "))


def make_notation(number, notation):
    num = ""

    if notation != 16:
        while number > 0:
            remainder = number % notation
            num = str(remainder) + num
            number //= notation

    else:
        while number > 0:
            remainder = number % notation
            if remainder < 10:
                num = str(remainder) + num
            else:
                if remainder == 10:
                    num += "A"
                elif remainder == 11:
                    num += "B"
                elif remainder == 12:
                    num += "C"
                elif remainder == 13:
                    num += "D"
                elif remainder == 14:
                    num += "E"
                elif remainder == 15:
                    num += "F"
            number //= notation

    return num


binary = make_notation(number, 2)
octan = make_notation(number, 8)
hexa = make_notation(number, 16)

if number < 1:
    print("Неверный ввод")
else:
    print(binary, octan, hexa, sep=", ")
