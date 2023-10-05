"""Objective : to modify the list to give the highest number in AP"""


def increment(list2):
    for i in range(len(list2)):
        list2[i] += 1


def count_substring_with_increment(string):
    lst = list()
    for i in range(len(string)):
        lst.append(string.find(" ", i))
    lst = list(set(lst))
    if -1 in lst:
        lst.remove(-1)
        increment(lst)
    else:
        pass
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > 1:
            print("i-value", i - 1)
            print("list-value", lst[i - 1])
    print(lst)


"""Experiment code 2 """
"""Objective : Maintain line space"""
name = "Chris   alan  pogba  "
count_substring_with_increment(name)

# !! Error as we try to assign values of def count_substring_with_increment we get a NoneType.
# m = count_substring_with_increment(name)
# print(type(m))
