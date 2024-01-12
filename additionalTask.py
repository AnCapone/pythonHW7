# Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ,
# довжина пароля – від 8 до 16 символів)

import re

while True:
    inputString = input("Введіть пароль (хоча б 1 велика, 1 маленька буква, цифра та символ. Від 8 до 16 символів: ")
    pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&;])[A-Za-z\d@$!%*#?&;]{8,16}'
    surnameName = re.fullmatch(pattern, inputString)
    if surnameName is None:
        print("Невірний формат вводу!")
        continue
    print("Введення вірне!")
    break