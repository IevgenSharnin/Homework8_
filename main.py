from datetime import date, datetime, timedelta

#today = (datetime(2021, 12, 27)).date()
today = date.today()
if today.weekday() == 0: # Коригуємо поточну дату, щоб забрати суботу-неділю,
    today = today - datetime.timestamp (days = 2) # якщо сьогодні понеділок

def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    # Змінні
    users_next_week = {} # Результат функції
    weekdays_indexes = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
                        3: 'Thursday', 4: 'Friday'}
    today = date.today()
#    today = (datetime(2021, 12, 27)).date()
    if today.weekday() == 0: # Коригуємо поточну дату, щоб забрати суботу-неділю,
        today = today - timedelta (days = 2) # якщо сьогодні понеділок

    # Перевірка на пустий список, що прийшов як аргумент 
    if users == []:
        return users_next_week

    # Проганяємо users через цикл та заповнюємо словник
    for person in users:
        print ((today - person.get('birthday')).days)
        today_wo_year = today - datetime(today.year, 1, 1).date()
        user_bday = person.get('birthday') - datetime(person.get('birthday').year, 1, 1).date()
        delta_to_today = today - datetime(today.year, person.get('birthday').month, 
                                     person.get('birthday').day).date()
        print (today_wo_year, user_bday, delta_to_today)
        if 0 >= delta_to_today.days >= -7:
            day_of_week_birth_today_year = datetime(today.year, person.get('birthday').month, 
                                     person.get('birthday').day).weekday
            print(datetime(today.year, person.get('birthday').month, 
                                     person.get('birthday').day).weekday)
            print (person.get('birthday'), day_of_week_birth_today_year)
            if day_of_week_birth_today_year == 5 or day_of_week_birth_today_year == 6:
                day_of_week_birth_today_year = 0
            list_for_append = users_next_week.get (weekdays_indexes.get(day_of_week_birth_today_year), [])
            list_for_append.append (person.get('name'))
            users_next_week.update ({weekdays_indexes.get(day_of_week_birth_today_year):
                                          list_for_append})

    return users_next_week


if __name__ == "__main__":
    users = [
            {
                "name": "Alice",
                "birthday": (datetime(2019, 11, 6)).date(),
            },
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")