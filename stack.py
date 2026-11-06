
name = "BASTATAS"
stack = []

print("===== STACK DATA STRUCTURE =====")
print("Name:", name)

# ADD PHASE (PUSH)
print("\n--- PUSHING LETTERS ---")

for letter in name:
    stack.append(letter)
    print("Pushed:", letter)
    print("Stack:", stack)

# REMOVE PHASE (POP)
print("\n--- POPPING LETTERS ---")

while len(stack) > 0:
    removed = stack.pop()
    print("Popped:", removed)
    print("Stack:", stack)

print("\nStack is empty!")
