# define list
list = ["1", "114", "11", "Rohit", "Rahul", "Virat", "Pant", "pantaloons"]
dict = {"Hardik": "123", "Rohit": "355", "Mbappe": "7", "114": "A"}
for i in list:
    for k, v in dict.items():
        if i == k :
            ind = list.index(i)
            list[ind] = v
print(list)

# for k, v in d.items():
#     for i in l:
#         if k in i:
#             ind = l.index(i)
#             l[ind] = v
# print(l)
