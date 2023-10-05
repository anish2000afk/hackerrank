#'chrome://vivaldi-webui/startpage?section=Speed-dials&background-color=#384d67'  !! The program automatically takes the range of the string.
# string = "ABCDAB"
# sub = "AB"
# count = int()
# for sub in string:
#     count += 1
#     print("TRU")
#     print(count)

# !! Trying to solve the problem with indices
# indices = []
# ele = "ANI"
# str = "ANISH"
# count = 0
# for i in range(len(str)):
# ~ The if statement will always be true.
#     if ele in str:
#         indices.append(i)
#         count = count + 1
# print(indices)
# print(count)

# !! Grabbing all index values that match the substring list.
# indices = []
# ele = "CDC"
# str = "ABCDCDC"
# count = 0
# for i in range(len(str)):
#     if str[i] in ele:
#         indices.append(i)
#         count = count + 1
# print(indices)
# print(int(count / len(ele)))

# !! Using the find method.
ele = "CDC"
str = "ABCDCDCDC"
for i in range(len(str)):
    x = str.find(ele)
    print(x)
