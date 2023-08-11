"""The main file"""

N = int(input())
ASC = N + 96
Row_val = N - 1  # The number of rows
thickness = (N * 2) - 2  # The thickness of one side
lis = list()
# for i in range(N):# Why did this now work
for i in range(N - 1, 0, -1):  # This works fine
    for n in range(0, N - 1, i):  # To-do continue from here
        print(n)
        ele = chr(ASC - n)  #
        lis.append(ele)
    print(lis)
