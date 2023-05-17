# def print_full_name(first, last):
#     for i in range(2):
#         first = input()
#         last = input()
#     string = "Hello", first, " ", last, "! You have delved into python."
#     return print(string)

'''Without the function '''
# def first_and_last(first, last):
#     first = str(input())
#     last = str(input())
#     print("Hello", first, last, "! You have delved into python.") 
# # Concatenation of ! in the last variable 
# first_and_last("anish", "kandulna") # The values will be strins.

first = input()
last = input()
def first_and_last(first, last):
    last = last+'!' # To remove indention space.
    return print("Hello", first, last, "You have delved into python.") 

first_and_last(first,last)

'''Goal : To join a variable value with a string'''
'''Example : a = anish 
Expected output = anish!'''
# a = 'anish'
# print(a+'!')

