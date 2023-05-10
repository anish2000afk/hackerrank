'''The original program for the nested list problem in hackerrank'''
records = []
u =[]
score_list = []
final_items = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    score_list.append(score)
    u = sorted(set(list(u)).union(set(score_list))) # removes duplicates and sorts the list of floats.
second_last = list(u)[1] # grabs the second last item
for i,m in records:
    for j in i,m:
        if j == second_last:
            final_items.append(i)
final_items.sort()
for i in final_items:
    print (i)
