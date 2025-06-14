import random

def get_numbers_ticket(min_num, max_num, quantity):
    """
    Генерує список унікальних випадкових чисел у заданому діапазоні.

    Параметри:
    min_num (int): Мінімальне число (не менше 1)
    max_num (int): Максимальне число (не більше 1000)
    quantity (int): Кількість чисел для вибору (не більше ніж кількість чисел у діапазоні)

    Повертає:
    list: Відсортований список унікальних випадкових чисел, або порожній список, якщо параметри некоректні.
    """
    # Перевірка: чи всі значення у межах дозволених обмежень
    if not (1 <= min_num <= max_num <= 1000) or quantity > (max_num - min_num + 1):
        return []

    # Генеруємо унікальні випадкові числа та сортуємо їх
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)

# Приклад виклику функції з параметрами для лотереї 6 із 49
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

