# The below code solves leap year for all years except 1992
def is_leap(n):
    leap = False
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                leap = True

    return leap


year = int(input())
print(is_leap(year))
