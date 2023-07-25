thickness = int(input())
c = "H"
# Top cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
    # The important bit here is the (thickness - 1)
    # It represents the max allocation space for c or 'H'

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
    # The actual ratio of their thickness if ( n= 4) is 2:12:10 i.e.> 1:6:5
