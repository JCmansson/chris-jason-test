"""
Loop Practice - Simple Examples
Practice reading and understanding for and while loops
"""

print("=" * 60)
print("LOOP PRACTICE EXAMPLES")
print("=" * 60)

# ============================================================================
# FOR LOOPS - Use when you know what to iterate over
# ============================================================================

print("\n--- EXAMPLE 1: Simple For Loop Through a List ---")
cities = ["Stockholm", "London", "Paris", "Tokyo"]

for city in cities:
    print(f"Visiting {city}")

# What this does:
# - Takes each item from the cities list
# - Assigns it to variable 'city'
# - Runs the indented code for each item

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 2: For Loop with Range (Counting) ---")

# Count from 0 to 4
for i in range(5):
    print(f"Count: {i}")

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

print("\nCounting by 2s (even numbers):")
for i in range(0, 11, 2):
    print(f"Even: {i}")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 3: For Loop with Index (enumerate) ---")
students = ["Alice", "Bob", "Charlie"]

for index, student in enumerate(students):
    print(f"Student #{index + 1}: {student}")

# What enumerate does:
# - Gives you both the index (position) and the item
# - index starts at 0, so we add 1 to make it human-friendly

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 4: For Loop Through Dictionary ---")
scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92
}

print("Student scores:")
for name, score in scores.items():
    print(f"{name}: {score} points")

    # Check if honor roll (90+)
    if score >= 90:
        print(f"  → {name} made honor roll!")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 5: For Loop Building a New List ---")
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    result = num * 2
    doubled.append(result)
    print(f"{num} × 2 = {result}")

print(f"\nOriginal: {numbers}")
print(f"Doubled: {doubled}")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 6: For Loop with Conditions ---")
grades = [45, 67, 89, 92, 55, 78, 41, 95]

print("Checking grades (passing = 50+):")
passing_count = 0
failing_count = 0

for grade in grades:
    if grade >= 50:
        print(f"{grade} - PASS")
        passing_count += 1
    else:
        print(f"{grade} - FAIL")
        failing_count += 1

print(f"\nPassing: {passing_count}")
print(f"Failing: {failing_count}")

input("\nPress Enter to continue...")

# ============================================================================
# WHILE LOOPS - Use when you don't know how many iterations needed
# ============================================================================

print("\n--- EXAMPLE 7: Simple While Loop (Countdown) ---")
count = 5

while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # IMPORTANT: Must change the condition or infinite loop!

print("Blast off!")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 8: While Loop Until Condition Met ---")
balance = 100
price = 15
items_bought = 0

print(f"Starting balance: ${balance}")
print(f"Item price: ${price}")

while balance >= price:
    balance -= price
    items_bought += 1
    print(f"Bought item {items_bought}. Balance: ${balance}")

print(f"\nTotal items bought: {items_bought}")
print(f"Remaining balance: ${balance}")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 9: While Loop with Break ---")
# Find first number divisible by 7

number = 50
found = False

while number <= 100:
    if number % 7 == 0:
        print(f"Found it! {number} is divisible by 7")
        found = True
        break  # Exit loop immediately
    number += 1

if not found:
    print("No number found")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 10: While Loop with Continue ---")
# Print numbers 1-10 but skip multiples of 3

number = 0

while number < 10:
    number += 1

    if number % 3 == 0:
        continue  # Skip rest of loop, go to next iteration

    print(f"Number: {number}")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 11: Nested Loops (Loop Inside Loop) ---")
# Multiplication table

print("Multiplication Table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{i} × {j} = {result:2d}", end="  ")  # end="" keeps on same line
    print()  # New line after each row

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 12: Practical Example - Calculate Total ---")
# Shopping cart with loop

cart = [
    {"item": "Apple", "price": 1.50, "quantity": 4},
    {"item": "Bread", "price": 2.99, "quantity": 2},
    {"item": "Milk", "price": 3.49, "quantity": 1},
    {"item": "Eggs", "price": 4.99, "quantity": 2}
]

total = 0

print("Shopping Cart:")
print("-" * 40)

for item in cart:
    item_total = item["price"] * item["quantity"]
    total += item_total

    print(f"{item['item']:10s} - ${item['price']:5.2f} × {item['quantity']} = ${item_total:6.2f}")

print("-" * 40)
print(f"TOTAL: ${total:.2f}")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 13: While Loop - Retry Logic ---")
# Simulate trying to connect (max 3 attempts)

max_attempts = 3
attempt = 0
connected = False

while attempt < max_attempts and not connected:
    attempt += 1
    print(f"Connection attempt {attempt}...")

    # Simulate connection (fails first 2 times, succeeds on 3rd)
    if attempt == 3:
        connected = True
        print("✓ Connected successfully!")
    else:
        print("✗ Connection failed, retrying...")

if not connected:
    print("Failed to connect after all attempts")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 14: For Loop - Find Maximum ---")
temperatures = [15, 22, 18, 25, 19, 21, 17]

highest = temperatures[0]  # Start with first temperature

for temp in temperatures:
    if temp > highest:
        highest = temp
    print(f"Current: {temp}°C, Highest so far: {highest}°C")

print(f"\nHighest temperature: {highest}°C")

input("\nPress Enter to continue...")

# ============================================================================

print("\n--- EXAMPLE 15: For Loop vs While Loop (Same Task) ---")

# Task: Print numbers 1-5

print("Using FOR loop:")
for i in range(1, 6):
    print(i)

print("\nUsing WHILE loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

print("\nBoth do the same thing! Use FOR when iterating over a collection.")

# ============================================================================

print("\n" + "=" * 60)
print("LOOP PRACTICE COMPLETE!")
print("=" * 60)
