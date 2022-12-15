print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2\n")

from A_QueueDataTypeClass import Queue1
fifo = Queue1()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())

print()
from A_QueueDataTypeClass import Queue2
fifo = Queue2("1st", "2nd", "3rd")
print(len(fifo))
print()
for element in fifo:
    print(element)
print()
print(len(fifo))
print()