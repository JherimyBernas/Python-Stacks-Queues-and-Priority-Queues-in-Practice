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

from E_CornerCasesInYourPriorityQueueClass import PriorityQueue1
messages1 = PriorityQueue1()
messages1.enqueue_with_priority(CRITICAL, wipers)
messages1.enqueue_with_priority(IMPORTANT, hazard_lights)
messages1.enqueue_with_priority(CRITICAL, Message("ABS engaged"))

from E_CornerCasesInYourPriorityQueueClass import PriorityQueue2
messages2 = PriorityQueue2()
messages2.enqueue_with_priority(CRITICAL, wipers)
messages2.enqueue_with_priority(IMPORTANT, hazard_lights)
messages2.enqueue_with_priority(CRITICAL, Message("ABS engaged"))
print()