from heapq import heappop, heappush

class PriorityQueue1:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)

class PriorityQueue2:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, value))

    def dequeue(self):
        return heappop(self._elements)[1]
