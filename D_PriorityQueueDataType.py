from QUEUES import PriorityQueue1, PriorityQueue2

print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2")
print("Building a Priority Queue Data Type")

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

print("\n-----------------------------------------------------------------------------------------------------------\n")
messages1 = PriorityQueue1()
messages1.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages1.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages1.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages1.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")
print(messages1.dequeue())

print("\n-----------------------------------------------------------------------------------------------------------\n")
messages2 = PriorityQueue2()
messages2.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages2.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages2.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages2.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")
print(messages2.dequeue())
print(messages2.dequeue())
print(messages2.dequeue())
print(messages2.dequeue())