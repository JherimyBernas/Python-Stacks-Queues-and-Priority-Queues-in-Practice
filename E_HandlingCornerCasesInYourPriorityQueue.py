print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE, YR. & SECTION: BSCOE 2-2\n")

from dataclasses import dataclass

@dataclass
class Message:
    event: str
wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")
print(wipers < hazard_lights)

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

from E_HandlingCornerCasesInYourPriorityQueueClass import PriorityQueue1
messages3 = PriorityQueue1()
messages3.enqueue_with_priority(CRITICAL, wipers)
messages3.enqueue_with_priority(IMPORTANT, hazard_lights)
messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))

from E_HandlingCornerCasesInYourPriorityQueueClass import PriorityQueue2
messages4 = PriorityQueue2()
messages4.enqueue_with_priority(CRITICAL, wipers)
messages4.enqueue_with_priority(IMPORTANT, hazard_lights)
messages4.enqueue_with_priority(CRITICAL, Message("ABS engaged"))
print()