
name = "BASTATAS"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None
tail = None

print("===== LINKED LIST DATA STRUCTURE =====")
print("Name:", name)

# ADD PHASE
print("\n--- ADDING LETTERS ---")

for letter in name:
    new_node = Node(letter)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

    print("Added:", letter)

    current = head
    values = []

    while current is not None:
        values.append(current.data)
        current = current.next

    print("Linked List:", values)


# REMOVE PHASE
print("\n--- REMOVING LETTERS ---")

while head is not None:
    removed = head
    head = head.next

    if head is None:
        tail = None

    print("Removed:", removed.data)

    current = head
    values = []

    while current is not None:
        values.append(current.data)
        current = current.next

    print("Linked List:", values)

print("\nLinked List is empty!")
