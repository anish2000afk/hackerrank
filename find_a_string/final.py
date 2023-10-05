"""We use the function given as sample"""


# def count_substring(string, sub_string):
#     return string.find(sub_string)


# count_substring("ABCDCDC", "CDC")

"""Experiment 1"""
# Defining num outside as a list allows us to access it
# Outside the for loop.
# num = list()
# string = "ABCDC"
# sub_string = "CDC"
# for i in range(len(sub_string)):
#     num = (string.find(sub_string))
# print(num)

"""Experiment 2 : Code that works !!! """
lst = []
string = "ABCDCDCDC"
sub_string = "CDC"
for i in range(len(string)):
    # We then manipulate the start parameter of find method using i.
    lst.append(string.find(sub_string, i))
lst = list(set(lst))
lst.remove(-1)
print(len(lst))
