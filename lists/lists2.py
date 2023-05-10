'''Goal : use split when there is only one arguement'''
n = int(input())
N = [1, 2 , 2]
for i in range(n):
    cd =input().split()
    if cd == 'print' :
        print(N)
    if cd == 'append':
        cd, integ = input().split()
        N.append(int(integ))
print(N)

# To-do 
# How to make print work using split() , if not possible change goals or seek alternatives.
