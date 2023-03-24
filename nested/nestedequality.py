matrix = [[j for j in range(5)]for i in range(5)]

greater_2 = [ _ for j in matrix for _ in j if (_>2)]
print(greater_2)
# for j in matrix:
#     for _ in j:
#         if (_ > 2):
#             print(_):
