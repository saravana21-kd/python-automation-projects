import random

challenges = [
    "Prime number checker",
    "Palindrome checker",
    "String reverser",
    "Number guessing game",
    "Largest number in list",
    "Simple calculator",
    "Count vowels in string",
    "Fibonacci generator",
    "Even or odd checker",
    "Custom list sorter"
]

challenge = random.choice(challenges)

print("\n=== Programming Challenge Generator ===\n")
print("Your challenge today:\n")
print("->", challenge)