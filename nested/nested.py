'''The original program for the nested list problem in hackerrank'''
records = []
u =[]
score_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    score_list.append(score)
    u = set(list(u)).union(set(score_list))
second_last = list(u)[-2]
names = [i for j in records for i in j if i == second_last]
print(names)
