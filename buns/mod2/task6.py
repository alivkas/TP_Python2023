site = input("Введите адрес сайта ")


def find_method(string, target):
    for i in range(len(string)):
        if string[i:i+len(target)] == target:
            return i
    return -1


while True:
    dot_index = find_method(site, ".")
    if dot_index == -1:
        print(site)
        break
    domain = site[:dot_index]
    print(domain)
    site = site[dot_index + 1:]
