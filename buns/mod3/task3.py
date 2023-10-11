site = input("Введите доменное имя сайта ").split(".")[::-1]
for domen in site:
    print(domen)