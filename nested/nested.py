records = []
u = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    u.append(score)
    u = sorted(u, reverse=True)
    k = set(u)
    k = k.union(k)
print(k)
