print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])

'''is equivalent to '''

results = []
for x in [1, 2, 3]:
     for y in [4, 5, 6]:
         results.append([x, y])

print(results)
