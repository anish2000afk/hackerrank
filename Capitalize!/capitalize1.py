"""Experiment code 1 : Kinda works"""
# new_lst = list()
# name = "Chris alan"
# name = name.split()
# for i in name:
#     new_lst.append(i.capitalize())

"""Using a previous definition"""


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
    print(lst)


"""Experiment code 2 """
"""Objective : Maintain line space"""
name = 'Chris   alan  pogba  '
lst = list()
count_substring_with_increment(name)
