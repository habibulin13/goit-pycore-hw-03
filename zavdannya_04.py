from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    in_7_days = today + timedelta(days=7)
    result = []

    for user in users:
        # Перетворюємо дату народження у форматі 'рік.місяць.день' на об'єкт datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Створюємо дату народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо вже минуло — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження в межах наступних 7 днів
        if today <= birthday_this_year <= in_7_days:
            congrat_date = birthday_this_year

            # Якщо це субота або неділя — переносимо на понеділок
            if congrat_date.weekday() == 5:  # Субота
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6:  # Неділя
                congrat_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })

    return result

users = [
      {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Cooper", "birthday": "1975.01.28"},
    {"name": "Bob Marley", "birthday": "1945.01.29"},
    {"name": "Test Guy", "birthday": "1992.06.15"},  
    {"name": "Test Girl", "birthday": "1992.06.19"},  
]



upcoming = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming)
