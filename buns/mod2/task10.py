string = input("Введите слова через пробел: ")
new_string = ""
last_letter = ""

for i in range(len(string)):
    if string[i] == " ":
        new_string += last_letter
        last_letter = ""
    else:
        last_letter = string[i]

new_string += last_letter

print(new_string)