domain = input("Введите доменное имя сайта: ")
current_domain = ""
previous_char = ""
current_position = len(domain) - 1

while current_position >= 0:
    char = domain[current_position]
    if char == ".":
        if previous_char != ".":
            print(current_domain[::-1])
            current_domain = ""
    else:
        current_domain += char
    previous_char = char
    current_position -= 1

print(current_domain[::-1])