def LeapYear(Year):
    if (Year % 4 == 0):
        if (Year % 100 == 0):
            return False
        else:
            return True
    else: 
        return False