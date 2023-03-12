# For orignial question visit : https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
x = 1
y = 1
z = 2
n = 3
# for i in range(0,x+1) :
#     for j in range(0,y+1):
#         for k in range(0, z+1):
#             if ((i+j+k) !=n):
#                 print([i,j,k])

print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0, z+1) if ((i+j+k) !=n)])
