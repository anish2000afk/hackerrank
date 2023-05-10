lst =  []
n = int(input())
student_marks = {}
total = 0
count = 0
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks:
    for i in student_marks[query_name]:
        total += float(i)
        count = count + 1
    avg = float((total/count))
    avg = "%.2f" % avg 
    print(avg)

