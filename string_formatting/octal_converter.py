def oct_converter(n):
    n = int(n)
    i = 8
    list = []
    if n % 8 == 0:
        list.append(0)
    else:
        list.append(n % 8)
    while n // i >= 1:
        remainder = (n // i) % 8  # The zero-division error
        list.append(remainder)
        i = i * 8
    list = list[::-1]
    num = int(
        "".join(map(str, list))
    )  # This lines joins the integers in one single integer object.
    # it is possible that .join only works with string.
    print(num)


oct_converter(100)
