"""Here we try to integrate the finanalis with the the original code"""
"""Adding a list of lists in from string2 """

"""The main file"""

N = int(input())
ASC = N + 96
Row_val = N - 1  # The number of rows
thickness = (N * 2) - 2  # The thickness of one side
lis = list()
list1 = list()
# for i in range(N):# Why did this now work
for i in range(0, N - 1, 1):  # Number of Groups.
    # for i in range(0, N - 1, 1):
    for n in range(0, i, 1):
        ele = chr(ASC - n)  #
        lis.append(ele)
        # list1.append(lis)
# print(lis)
# print(list1)

"""Code to create a list of list from an list with a particular value"""
# test_list = [1, 4, 5, 6, 4, 5, 6, 5, 4]

# print("The original list : " + str(test_list))

# particular_value = 5
# result = []  # The over-arching list
# temp_list = []  # The internal list
# for i in test_list:
#     if i == particular_value: # splitting by a particular value
#         # In our case it is the variable "e"
#         temp_list.append(i)
#         result.append(temp_list)
#         temp_list = []  # Emptying the list
#     else:
#         temp_list.append(i)
# result.append(temp_list)
# print("The list after splitting by a value : " + str(result))

"""Application of the particular code with our list"""


print("The original list : " + str(lis))

particular_value = "e"
newlis = lis[::-1]  # Reversing the list to match particular value.
result = []  # The over-arching list
temp_list = []  # The internal list
for i in newlis:
    if i == particular_value:  # splitting by a particular value
        # In our case it is the variable "e"
        temp_list.append(i)
        result.append(temp_list)
        temp_list = []  # Emptying the list
    else:
        temp_list.append(i)
result.append(temp_list)
print("The list after splitting by a value : " + str(result))

"""https://www.geeksforgeeks.org/python-split-list-into-lists-by-particular-value/"""

"""Now we reverse the list of lists"""

finallis = []
for i in result:
    # for v in i:
    newlist = i[::-1]
    finallis.append(newlist)
finallis.pop()
finallis.reverse()
print("The final list should look like this", finallis)

# Integration with code from above.
"""If we want the character in the upper half"""
for i in range(Row_val):
    print(
        (finallis[i][i]).rjust(thickness, "-")  # We want a string type.
        # The above code would also not work.
        + " "
        + chr(ASC - i)
        + " "
        + (i * chr(ASC - i - 1)).ljust(thickness, "-")
    )

# Conclusion : we want a workaround this attribute error.
# See you next week :)
# Present date : 2023-08-30 12:45
# Restart date : 2023-09-06
# Reason : Over a week.
