print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2\n")

from D_BuildingPriorityQueueDataTypeClass import PriorityQueue1
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1
messages1 = PriorityQueue1()
messages1.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages1.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages1.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages1.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")
print(messages1.dequeue())
print()

from D_BuildingPriorityQueueDataTypeClass import PriorityQueue2
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1
messages2 = PriorityQueue2()
messages2.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages2.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages2.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages2.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")
print(messages2.dequeue())
print(messages2.dequeue())
print(messages2.dequeue())
print(messages2.dequeue())
print()