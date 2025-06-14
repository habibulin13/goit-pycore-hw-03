from datetime import datetime

def get_days_from_today(date_str):
    """
    Обчислює кількість днів між поточною датою і заданою датою у форматі 'YYYY-MM-DD'.

    Параметри:
    date_str (str): Рядок дати у форматі 'РРРР-ММ-ДД'

    Повертає:
    int: Різниця у днях (може бути від’ємною, якщо дата в майбутньому)
    str: Повідомлення про помилку, якщо формат неправильний
    """
    try:
        # Перетворюємо рядок у об'єкт дати (без часу)
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
        # Обчислюємо різницю з поточною датою
        return (datetime.today().date() - d).days
    except ValueError:
        # Обробка помилки, якщо вхідний формат неправильний
        return "Неправильний формат дати. Має бути 'YYYY-MM-DD'"

# Ввід дати користувачем
date_input = input("Введіть дату у форматі YYYY-MM-DD: ")
# Вивід результату
print(get_days_from_today(date_input))


