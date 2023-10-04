phone = input("Введите номер телефона ")

new_phone = phone.replace("-", "").replace(")", "").replace("(", "").replace(" ", "")
print(new_phone)
