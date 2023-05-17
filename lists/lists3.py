'''Goal : to test input() .split()'''

# name , *line = input().split()
# print(name)
'''Conclusion : it also works in case of single argument.'''

'''Goal : to test input() and split() '''
# N = []
# name , *line = input().split()
# if name ==  'insert' :
#     scores = list(map(int, line)) # mapping the args in a list of integers
#     N.insert(scores[0], scores[1]) # since we have 2 integer arguments we can map as places 0 and 1.
#     print(N)

'''Goal : to test remove function'''
list= [1 , 2 , 3 , 1, 5]
list.remove(1)
print(list)
