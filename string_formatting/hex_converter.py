def hex_iterator(n):
    dict = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    n = int(n)
    i = 16
    list = []
    if n % 16 == 0:
        list.append(str('0'))
    else:
        list.append(str(n % 16))
    while n // i >= 1:
        remainder = (n // i) % 16  # The zero-division error
        list.append(str(remainder))
        i = i * 16
    list2 = list[::-1]
    # Until here it genetrates a list and reversed it.
    # for i in list:

    for i in list2:
        for k, v in dict.items():
            if i == k:
                ind = list2.index(i)
                list2[ind] = v
    # print('found it')
    # print(i)
    num = ''.join(map(str, list2))
    # This lines joins the integers in one single integer object.
    # it is possible that .join only works with string.
    print(num)
