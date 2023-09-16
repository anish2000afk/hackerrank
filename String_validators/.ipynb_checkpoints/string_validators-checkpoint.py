s = input()
print(s.isalnum())

for i in s:
    print(i)
    if i.isalpha():
        print(s.isalpha())
    if i.isdigit() == True:
        print(i.isdigit())
    if i.islower() == True:
        print(s.islower())
    if i.isupper() == True:
        print(s.isupper())


