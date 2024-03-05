from datetime import datetime

def get_days_from_today():
    current_date = datetime.today()
    today_date = current_date.date()
    user_date = input('Enter date: ')
    try:
        date_for_difference = datetime.strptime(user_date, "%Y.%m.%d")
    except ValueError:
        return print(f'{user_date} the date format is not correct, try this format "2024.04.01"')    
    
    date_difference = date_for_difference.toordinal() - today_date.toordinal()
    return int(date_difference)

print(get_days_from_today())

