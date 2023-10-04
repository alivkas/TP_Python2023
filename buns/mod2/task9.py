string = input("Введите строку ")
vowels = 0
consonants = 0

for sym in string:
    if sym in "аеёиоуыэюя":
        vowels += 1
    if sym in "бвгджзйклмнпрстфхцчшщ":
        consonants += 1

print(vowels, consonants, sep=" ")