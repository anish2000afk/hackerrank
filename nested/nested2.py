'''Nested list comprehension to grab items on score'''    

records = []
u = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    score_list =[i for j in records for i in j if type(i) == float ]
print(score_list)

