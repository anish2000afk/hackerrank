'''We could make this code a lot smaller using functions or even a new goal'''
s = input()
d = []
f = []
h = []
g = []
l = []
sout = str()
for i in s:
    d.append(str((i.isalnum())))
    if 'True' in d:
        sout = 'True'
    else:
        sout = 'False'
print(sout)
for i in s:
    f.append(str((i.isalpha())))
    if 'True' in f:
        sout = 'True'
    else:
        sout = 'False'
print(sout)
for i in s:
    l.append(str((i.isdigit())))
    if 'True' in l:
        sout = 'True'
    else:
        sout = 'False'
print(sout)
for i in s:
    h.append(str((i.islower())))
    if 'True' in h:
        sout = 'True'
    else:
        sout = 'False'
print(sout)
for i in s:
    g.append(str((i.isupper())))
    if 'True' in g:
        sout = 'True'
    else:
        sout = 'False'
print(sout)

