print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2\n")

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

from dataclasses import dataclass
@dataclass
class Message:
    event: str
wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")
print(wipers < hazard_lights)

from QUEUES import PriorityQueue2
messages1 = PriorityQueue2()
messages1.enqueue_with_priority(CRITICAL, wipers)
messages1.enqueue_with_priority(IMPORTANT, hazard_lights)
messages1.enqueue_with_priority(CRITICAL, Message("ABS engaged"))

from QUEUES import PriorityQueue3
messages2 = PriorityQueue3()
messages2.enqueue_with_priority(CRITICAL, wipers)
messages2.enqueue_with_priority(IMPORTANT, hazard_lights)
messages2.enqueue_with_priority(CRITICAL, Message("ABS engaged"))
print()