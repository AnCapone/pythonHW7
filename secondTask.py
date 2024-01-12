# Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
import re

while True:
    inputString = input("Введіть номер мобільного телефону в форматі 12 цифр з \"+\" або без \"+\" попереду: ")
    mobilePhoneNumber = re.fullmatch(r'([+]\d{12})|(\d{12})', inputString)
    if mobilePhoneNumber is None:
        print("Невірний формат вводу!")
        continue
    print("Формат введення вірний!")
    break