def hex_converter(n):
    dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    n = int(n)
    i = 16
    list = []
    if n % 16 == 0:
        list.append(0)
    else:
        list.append(n % 16)
    while n // i >= 1:
        remainder = (n // i) % 16  # The zero-division error
        list.append(remainder)
        i = i * 16
    list = list[::-1]
    num = int(
        "".join(map(str, list))
    )  # This lines joins the integers in one single integer object.
    # it is possible that .join only works with string.
    print(num)


hex_converter(100)
