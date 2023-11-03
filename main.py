from datetime import date, datetime


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    # Змінні
    users_birth_next_week = {} # Результат функції
    weekdays_indexes = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
                        3: 'Thursday', 4: 'Friday'}
    today = date.today()
    if today.weekday() == 0: # Коригуємо поточну дату, щоб забрати суботу-неділю,
        today = today - datetime.timestamp (days = 2) # якщо сьогодні понеділок

    # Перевірка на пустий список, що прийшов як аргумент 
    if users == []:
        return users_birth_next_week

    # Проганяємо users через цикл та заповнюємо словник
    for person in users:
        if person.get('birthday') >= today:
            day_of_week_birth = person.get('birthday').weekday()
            if day_of_week_birth == 5 or day_of_week_birth == 6:
                day_of_week_birth = 0
            list_before_append = users_birth_next_week.get (weekdays_indexes.get(day_of_week_birth), [])
            list_before_append.append (person.get('name'))
            users_birth_next_week.update ({weekdays_indexes.get(day_of_week_birth):
                                          list_before_append})

    return users_birth_next_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2023, 11, 3).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")