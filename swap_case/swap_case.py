# To-do > Make a proper notes on it on Jupyter-lab.
def swap_case(s):
    N = []
    for i in s:
        swap = ord(i)
        if swap in range(65,90):
            N.append(i.lower())
        elif swap in range(97, 122):
            N.append(i.upper())
        else:
            N.append(i)
    final = ''.join(N)
    return print(final)
# possible problem is here as we need to store the new and converted string; rather we are displaying the old string.
# possible solution is to first store the converted values in a list.
# Another problem is to deal with spaces.
# Possible solution is to an else statement.
# Also to make to flatten a list.
# Possible solution would be to use .join() function.
# Also remove the return print(final) to return final. Other wise you will get a None Line.
# Also when using range the second argument is upto but not including.
s = 'SG.2ehL62pSmsnd7c9XYYsFvV067gybBhsSM0SJ7zpAJWr8pwEFzq3ACtuSAjpL7ZnWXbASGlBnEawSnWs1 gpCySKB2.at bt5S'
swap_case(s)

'''Tried without a function'''
# s= 'anish'
# for i in s:
#     swap = ord(i)
#     for swap in range(65,90):
#         i.lower()
#     for swap in range(97, 122):
#         i.upper()
#         print(s)

'''Simplest version using ord'''
# s = 'a'
# swap = ord(s)
# print(type (swap))
# for i in s:
#     print(ord(i))
#     if swap in range(65,98):
#         print(s.upper())
    
'''Finding ord values'''
# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))
