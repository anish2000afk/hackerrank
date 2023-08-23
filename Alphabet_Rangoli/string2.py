"""The main file"""

N = int(input())
ASC = N + 96
Row_val = N - 1  # The number of rows
thickness = (N * 2) - 2  # The thickness of one side
lis = list()
# for i in range(N):# Why did this now work
for i in range(0, N, 1):  # Number of Groups.
    # for i in range(0, N - 1, 1):
    for n in range(0, i, 1):
        print("n-value", n)
        print("i-value", i)
        print("ASCII value", ASC - n)
        ele = chr(ASC - n)  #
        print(ele)
        lis.append(ele)
    print(lis)
