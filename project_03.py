# A–Z = 65 – 90
# a–z = 97 – 122
# 0–9 = 48 – 57
# symbols = 32-64 + 91-96 + 123-126

import random

characters = int(input("How many Letters would you like in your Password?\n"))
numbers = int(input("How many Numbers would you like in your Password?\n"))
symbols = int(input("How many Symbols would you like in your Password?\n"))

password = []

symbol_range = list(range(32, 65)) + list(range(91, 97)) + list(range(123, 127))

password_length = characters + numbers + symbols

for _ in range(password_length):
    choices = []

    if characters > 0:
        choices.append(0)
    if numbers > 0:
        choices.append(1)
    if symbols > 0:
        choices.append(2)

    value = random.choice(choices)
    match (value):
        case 0:
            characters -= 1
            password.append(
                chr(
                    random.randint(97, 122)
                    if random.choice([True, False])
                    else random.randint(65, 90)
                )
            )
        case 1:
            numbers -= 1
            password.append(str(random.randint(0, 9)))
        case 2:
            symbols -= 1
            password.append(chr(random.choice(symbol_range)))


print("Password is '", "".join(password), "'")
