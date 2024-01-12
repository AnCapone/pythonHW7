# домашній номер телефону (тільки цифри та довжина номера)
import re

while True:  # бескінечний цикл
    homePhoneNumber = re.fullmatch(r'\d{7}', input("Введіть номер телефону без коду (7 цифр без пробілів): "))
    if homePhoneNumber is None:
        print("Невірний формат вводу!")
        continue
    print("Введення вірне!")
    break
