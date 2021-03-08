def calcYear(year):
    try:
        year = int(year)
    except:
        return "Not a leap year"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                return "Not a leap year"
        return "Leap year"
    else:
        return "Not a leap year"