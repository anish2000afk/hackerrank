length, thickness = input().split()
length = int(length)
thickness = int(thickness)
thick2 = int(thickness // 3)
c = ".|."
for i in range(length // 2):
    print(
        (c * i).rjust((thickness // 2) - 1, "-")
        + c
        + (c * i).ljust((thickness // 2) - 1, "-")
    )
print(("WELCOME").center(thickness, "-"))
for i in range(length // 2):
    print(
        (c * ((thick2 // 2) - 1 - i)).rjust(thickness // 2 - 1, "-")
        + c
        + (c * ((thick2 // 2) - 1 - i)).ljust(thickness // 2 - 1, "-")
    )
