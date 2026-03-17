import random
from pathlib import Path

# Ensure quotes.txt is loaded relative to this script, not the current working directory
script_dir = Path(__file__).resolve().parent
quotes_path = script_dir / "quotes.txt"

with quotes_path.open("r", encoding="utf-8") as file:
    quotes = file.readlines()

quote = random.choice(quotes)

print("\n💡 Quote of the Day:\n")
print(quote)
