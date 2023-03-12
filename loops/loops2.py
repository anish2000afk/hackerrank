n = int(input("Enter a number:"))
if (n<=150):
    for i in range(1,n+1):
         print(i, end="")


# for function of sep go https://www.geeksforgeeks.org/python-sep-parameter-print/
# for function of end  https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
'''
The questions to be asked were 
1> We want the output to be a string.
2> How to also print user entered digits? eg> n = 5 , s output = 12345
'''

'''
The answer to 1 is not a surety as print statement returns a string.
The answer to 2 is that we just do n+1.
'''
