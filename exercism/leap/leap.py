def is_leap_year(year):
        """ Function that checks if a year is a leap year. """
        # if (year % 400 == 0):
        #     return True
        # elif (year % 100 == 0):
        #     return False
        # elif (year % 4 == 0):
        #     return True
        # else:
        #     return False
        return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
