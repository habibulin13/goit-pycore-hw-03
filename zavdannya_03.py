import re

def normalize_phone(phone_number):
    # Залишаємо лише цифри
    digits = re.sub(r'\D', '', phone_number)

    # Якщо номер починається з '380' — додаємо '+'
    if digits.startswith("380"):
        return '+' + digits
    # Якщо номер починається з '0' — додаємо '+38'
    elif digits.startswith("0"):
        return '+38' + digits
    # Якщо номер уже має правильний формат (наприклад, +380...)
    elif phone_number.strip().startswith('+'):
        return '+' + digits
    # Якщо щось інше — все одно додаємо '+38' про всяк випадок
    else:
        return '+38' + digits

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
