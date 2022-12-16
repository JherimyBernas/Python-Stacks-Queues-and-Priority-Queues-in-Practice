from heapq import heappop, heappush

print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2")
print("Representing Priority Queues With a Heap")

print("\n-----------------------------------------------------------------------------------------------------------\n")
fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")
print(fruits)
print()

print("\n-----------------------------------------------------------------------------------------------------------\n")
print(heappop(fruits))
print(fruits)
print()

print("\n-----------------------------------------------------------------------------------------------------------\n")
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)
print(person1 < person2)
print(person2 < person3)
print()