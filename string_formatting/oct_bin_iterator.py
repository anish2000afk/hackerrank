from string_format import iterator 
from decimal_to_binary_converter import converter
from octal_converter import oct_converter

n = int(input())
iterator(n) # The iterator will not have a for loop as it might duplicate data.
for i in range(1,n+1):
    converter(i)
for i in range(1,n+1):
    oct_converter(i)
