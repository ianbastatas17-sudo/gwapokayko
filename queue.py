
from collections import deque

name = "BASTATAS"
queue = deque()

print("===== QUEUE DATA STRUCTURE =====")
print("Name:", name)

# ADD PHASE (ENQUEUE)
print("\n--- ENQUEUING LETTERS ---")

for letter in name:
    queue.append(letter)
    print("Enqueued:", letter)
    print("Queue:", list(queue))

# REMOVE PHASE (DEQUEUE)
print("\n--- DEQUEUING LETTERS ---")

while len(queue) > 0:
    removed = queue.popleft()
    print("Dequeued:", removed)
    print("Queue:", list(queue))

print("\nQueue is empty!")
