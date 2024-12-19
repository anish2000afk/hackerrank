# Final solution
def is_leap(n):
    leap = False
    if n % 4 == 0:
        leap = True  # Leap = 1
        if n % 100 == 0:
            leap = False  # Leap = 0
            if n % 400 == 0:
                leap = True  # Leap = 1

    return leap


year = int(input())
print(is_leap(year))


# TODO Additional question : WAP with and operator
