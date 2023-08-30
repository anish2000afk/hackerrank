"""Reversing the elements of list of list."""
list1 = [["a", "b", "c"], ["a", "b"], ["a"]]
'''Expected output : [["a"],["b", "a"],["c", "b", "a"]]'''
lis = []
for i in list1:
    # for v in i:
    newlist = i[::-1]
    lis.append(newlist)
lis.reverse()
print(lis)
