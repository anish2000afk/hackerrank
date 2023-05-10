"""This sandbox's obj is to print the only anish from the nested list"""
list = [['foden', 30.0],['kyle', 2.0],['anish', 2.0]]
final_items = []
item = 2.0
for i,m in list:
    for j in i,m:
        if j == item:
            final_items.append(i) # Make another list to append the required names
final_items.sort()
for i in final_items:
    print(i)

"""To make it work in a list-comprehension"""
# final_items =  [[i for i,m in list] for j in i,m]
# print(final_items)
"""We could just use an if statement looking for a string"""


