s = input()
g = []
for i in s:
    g.append((i.isdigit()))
    if 'True' in g:
        print('True')
    else :
        print('False')
