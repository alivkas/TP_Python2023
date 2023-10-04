def shift_alphabet(char, num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    index = alphabet.index(char)
    shifted_index = (index + num) % len(alphabet)
    shifted_char = alphabet[shifted_index]

    return shifted_char


input_str = input("Введите символ и число: ")
slice = 0

for sym in input_str:
    if sym != ",":
        slice += 1
    else:
        break

char = input_str[0:slice:]
num = int(input_str[slice + 1:])

shifted_char = shift_alphabet(char, num)

print(shifted_char)