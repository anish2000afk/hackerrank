'''Goal: To separate a string from an integer'''
n = int(input())
N = []
for i in range(n):
    cd, *integ = input().split()
    scores = list(map(int, integ))
    if cd == 'insert':
        N.insert(scores[0], scores[1])
    if cd == 'append' :
        N.append(int(scores[0]))
    if cd == 'print' :
        print(N)
    if cd == 'remove':
        N.remove(int(scores[0]))
    if cd == 'sort':
        N.sort()
    if cd == 'pop':
        N.pop()
    if cd == 'reverse':
        N.reverse()
print(N)

 
