import random

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

quote = random.choice(quotes)

print("\n💡 Quote of the Day:\n")
print(quote)