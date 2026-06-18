from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "joined the queue")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
            return None

        return self.queue.popleft()


# Test
q = Queue()

q.enqueue("Asha")
q.enqueue("Ravi")
q.enqueue("Meena")

while len(q.queue) > 0:
    person = q.dequeue()
    print("Serving:", person)