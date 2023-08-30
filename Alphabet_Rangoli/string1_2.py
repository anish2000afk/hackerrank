"""The main file"""

N = int(input())
ASC = N + 96
Row_val = N - 1  # The number of rows
thickness = (N * 2) - 2  # The thickness of one side
lis = list()
# for i in range(Row_val):
#     print().rjust()

"""If we want the character in the upper half"""
for i in range(Row_val):
    for i in range(0, N - 1, 1):  # Number of Groups.
        # for i in range(0, N - 1, 1):
        for n in range(0, i, 1):
            ele = chr(ASC - n)  #
            print(
                (ele).rjust(thickness, "-")
                + " "
                + chr(ASC - i)
                + " "
                + (i * chr(ASC - i - 1)).ljust(thickness, "-")
            )
