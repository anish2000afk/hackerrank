"""The main file"""

N = int(input())
ASC = N + 96
Row_val = N - 1  # The number of rows
thickness = (N * 2) - 2  # The thickness of one side
# for i in range(Row_val):
#     print().rjust()

"""If we want the character in the upper half"""
for i in range(Row_val):
    print(
        (i * chr(ASC - i - 1)).rjust(thickness, "-")
        + " "
        + chr(ASC - i)
        + " "
        + (i * chr(ASC - i - 1)).ljust(thickness, "-")
    )
