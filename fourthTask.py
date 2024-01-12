# ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

import re

while True:
    inputString = input("Введіть прізвище, ім'я, по-батькові через пробіл ")
    surnameName = re.fullmatch(r'\w{2,20}\s\w{2,20}\s\w{2,20}', inputString)  # \w{2,20} - 2-20 буквених символів
                                                                                     # \s - пробіл
    if surnameName is None:
        print("Невірний формат вводу!")
        continue
    print("Введення вірне!")
    break