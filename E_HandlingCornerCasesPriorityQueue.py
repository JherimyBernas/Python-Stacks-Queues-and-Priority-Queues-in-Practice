from dataclasses import dataclass
from QUEUES import PriorityQueue2, PriorityQueue3

print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2")
print("Handling Corner Cases in Your Priority Queue")

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

@dataclass
class Message:
    event: str


wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")
print(wipers < hazard_lights)

messages1 = PriorityQueue2()
messages1.enqueue_with_priority(CRITICAL, wipers)
messages1.enqueue_with_priority(IMPORTANT, hazard_lights)
messages1.enqueue_with_priority(CRITICAL, Message("ABS engaged"))

messages2 = PriorityQueue3()
messages2.enqueue_with_priority(CRITICAL, wipers)
messages2.enqueue_with_priority(IMPORTANT, hazard_lights)
messages2.enqueue_with_priority(CRITICAL, Message("ABS engaged"))
print()