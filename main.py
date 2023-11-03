from datetime import date, datetime


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    users_dict = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 
                  'Thursday': [], 'Friday': []}
    if users == []:
        return users_dict
    
    return users_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")