from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    # Змінні
    users_next_week = {} # Результат функції
    weekdays_indexes = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
                        3: 'Thursday', 4: 'Friday'}
    today_ = date.today()
#    today_ = datetime(2023, 1, 2).date()
    if today_.weekday() == 0: # Коригуємо поточну дату, щоб забрати суботу-неділю,
        today_ = today_ - timedelta (days = 2) # якщо сьогодні понеділок
    if today_.weekday() == 6: # Коригуємо поточну дату, щоб забрати суботу,
        today_ = today_ - timedelta (days = 1) # якщо сьогодні неділя

    # Перевірка на пустий список, що прийшов як аргумент 
    if users == []:
        return users_next_week

    # Проганяємо users через цикл та заповнюємо словник
    for person in users:
        # Кількість днів від початку поточного року до сьогодні
        today_wo_year = today_ - datetime(today_.year, 1, 1).date()
        # Кількість днів від сьогодні до кінця року
        today_to_endyear = today_ - datetime(today_.year, 12, 31).date()
        # Кількість днів від початку року народження до дати народження
        user_bday = person.get('birthday') - datetime(person.get('birthday').year, 1, 1).date()
        # Дельта від сьогодні до дня народження без урахування року
        if (0 >= today_to_endyear.days > -7) and (user_bday.days < 7):
            delta_to_today = today_ - datetime(today_.year+1, person.get('birthday').month, 
                                     person.get('birthday').day).date()
        else:
            delta_to_today = today_ - datetime(today_.year, person.get('birthday').month, 
                                     person.get('birthday').day).date()
# Перевіряємо, що дата народження на наст.тижні і формуємо вихідний словник
        if 0 >= delta_to_today.days > -7:
            day_of_week_birth_today_year = datetime(today_.year, person.get('birthday').month, 
                                     person.get('birthday').day).weekday()
            if day_of_week_birth_today_year == 5 or day_of_week_birth_today_year == 6:
                day_of_week_birth_today_year = 0
            list_for_append = users_next_week.get (weekdays_indexes.get(day_of_week_birth_today_year), [])
            list_for_append.append (person.get('name'))
            users_next_week.update ({weekdays_indexes.get(day_of_week_birth_today_year):
                                    list_for_append})

    return users_next_week


if __name__ == "__main__":
    today_ = date.today()
    #today_ = datetime(2023, 1, 2).date()
    if today_.weekday() == 0: # Коригуємо поточну дату, щоб забрати суботу-неділю,
        today_ = today_ - timedelta (days = 2) # якщо сьогодні понеділок
    if today_.weekday() == 6: # Коригуємо поточну дату, щоб забрати суботу-неділю,
        today_ = today_ - timedelta (days = 1) # якщо сьогодні понеділок

    users = [
#            {
#                "name": "John",
#                "birthday": (today_ + timedelta(days=-5)),
#            },
#            {
#                "name": "Doe",
#                "birthday": (today_ + timedelta(days=-6)),
#            },
            {"name": "Alice", "birthday": (today_ + timedelta(days=3))},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
#    for day_name, names in result.items():
#        print(f"{day_name}: {', '.join(names)}")