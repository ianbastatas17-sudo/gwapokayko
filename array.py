
name = "BASTATAS"
array = []

print("===== ARRAY DATA STRUCTURE =====")
print("Name:", name)

# ADD PHASE
print("\n--- ADDING LETTERS ---")

for letter in name:
    array.append(letter)
    print("Added:", letter)
    print("Array:", array)

# REMOVE PHASE
print("\n--- REMOVING LETTERS ---")

while len(array) > 0:
    removed = array.pop()
    print("Removed:", removed)
    print("Array:", array)

print("\nArray is empty!")
