"""This code concerns
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem"""
# def __repr__(arr):
#     return str(arr)
"""The above 2 lines are failed attmepts to modify arr"""
# n = int(input())
# arr = map(int, input().split())
"""If you want to know more about map
https://www.simplilearn.com/tutorials/python-tutorial/map-in-python#:~:text=Map%20in%20Python%20is%20a,to%20the%20map%20in%20Pythonself.
    ~In my opinion it works more like a for loop """

# res = all((ele > 0 for ele in A))
"""Failed attempt with all()"""

"""For converting a list of any type to another type
https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/"""

n = int(input())
arr = input()
A = arr.split(" ")
A = list(map(int, A))  # we are using map function to convert this list to Integers.
if n in range(2, 11):
    for i in A:
        if i in range(-100, 101):
            u = sorted(set(A).union(set(A)))
