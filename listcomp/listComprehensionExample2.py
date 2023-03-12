ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10

'''is equivalent to '''

lis = []
for x in range(10) :
    if  x % 3 == 0:
        lis.append(x)
print(lis)
