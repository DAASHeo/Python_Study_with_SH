def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


##문제 3

day_31 = {1, 3, 5, 7, 8, 10, 12}

day_30 = {4, 6, 9, 11}

feb = {2}


def days_in_month(year, month):
    if month in day_31:
        return 31

    if month in day_30:
        return 30

    if month in feb:
        if is_leap_year(year):
            return 29
        else:
            return 28

