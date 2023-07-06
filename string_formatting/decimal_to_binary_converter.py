
def converter(n):
    n = int(n)
    i = 2
    list = []
    if (n%2 == 0):
        list.append(0)
    else:
        list.append(1)
    while (n//i >= 1):
            remainder = (n//i)%2 # The zero-division error
            list.append(remainder)
            i = i*2
    list = list[::-1]
    num = int(''.join(map(str,list))) # This lines joins the integers in one single integer object.
    # it is possible that .join only works with string.
    print(num)

