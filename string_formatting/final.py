from iterator import string_format
from decimal_to_binary_converter import converter
from octal_converter import oct_converter
from hex_converter import hex_iterator

n = int(input())
string_format(n)  # The iterator will not have a for loop as it might duplicate data.
for i in range(1, n + 1):
    oct_converter(i)
for i in range(1, n + 1):
    hex_iterator(i)
for i in range(1, n + 1):
    converter(i)
