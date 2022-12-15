print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2\n")

from B_BuildingStackDataTypeClass import Stack

lifo = Stack("1st", "2nd", "3rd")
for element in lifo:
    print(element)
print()

# We could probably get away with using a plain old Python list as a rudimentary stack
lifo = []
lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")
print(lifo.pop())
print(lifo.pop())
print(lifo.pop())
print()