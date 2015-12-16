from datetime import date, timedelta
from calendar import monthrange

class MeetupDayException(Exception):
    pass

days_of_week = {'Tuesday': 1, 'Monday': 0, 'Sunday': 6, 'Saturday': 5, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}

def last_match(year, month, day_of_week):
    last_day_of_month = date(year, month + 1, 1) - timedelta(days = 1)
    last_weekday = last_day_of_month.weekday()
    days_to_subtract = (last_weekday - days_of_week[day_of_week]) % 7
    return last_day_of_month - timedelta(days = days_to_subtract)

def first_match(year, month, day_of_week):
    first_day_of_month, nr_of_days_in_month = monthrange(year, month)
    first_match = (days_of_week[day_of_week] - first_day_of_month) % 7 + 1
    return first_match

def nth_match(first_match, n):
    return first_match + 7 * (n - 1)

def nth_weekday(year, month, day_of_week, n):
    first = first_match(year, month, day_of_week)
    nth = nth_match(first, n)
    try:
        return date(year, month, nth)
    except ValueError:
        raise MeetupDayException(
            "There is no {n}th {day_of_week} in {month} {year}"
            .format(n=n, day_of_week=day_of_week, month=month, year=year))

def teenths(year, month, day_of_week):
    for teenth in range(13, 20):
        current = date(year, month, teenth)
        if current.strftime("%A") == day_of_week:
            return current

def meetup_day(year, month, day_of_week, specification):
    if specification[0].isdigit():
        n = int(specification[0])
        return nth_weekday(year, month, day_of_week, n)
    elif specification == 'last':
        return last_match(year, month, day_of_week)
    elif specification == 'teenth':
        return teenths(year, month, day_of_week)
    else:
        raise NotImplementedError