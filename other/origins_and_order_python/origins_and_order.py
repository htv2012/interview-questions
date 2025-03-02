from itertools import permutations


def format_date(year, month, day):
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month in days_in_month and day > 0 and day <= days_in_month[month]:
        return '{:02}/{:02}/{:02}'.format(month, day, year)
    return None


def origins_and_order(a, b, c):
    seen = None

    for ymd in permutations((a, b, c)):
        formatted_date = format_date(*ymd)
        if formatted_date is None:
            continue

        if seen is None:
            seen = formatted_date
        elif seen != formatted_date:
            return 'Ambiguous'

    return seen
