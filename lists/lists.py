'''Goal: To separate a string from an integer'''
n = int(input())
N = []
for i in range(n):
    cd, integ = input().split()
    if cd == 'append' :
        N.append(int(integ))
    if cd == 'print' :
        print(N)
    if cd == 'remove ':
        N.remove(int(integ))
    if cd == 'sort':
        N.sort()
    if cd == 'pop':
        N.pop()
    if cd == 'reverse':
        N.reverse()

