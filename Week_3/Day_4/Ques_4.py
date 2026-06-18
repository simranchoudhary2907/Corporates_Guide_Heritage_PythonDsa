from collections import deque

queue = deque()

# Add people
queue.append("Asha")
queue.append("Ravi")
queue.append("Meena")
queue.append("Karan")
queue.append("Priya")

print("People entered the queue.\n")

while queue:
    person = queue.popleft()

    print(
        f"Serving: {person}. "
        f"Tickets remaining in queue: {len(queue)}"
    )

print("\nQueue is now empty.")