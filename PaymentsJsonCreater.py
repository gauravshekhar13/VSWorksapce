import json
import random

OUTPUT_FILE = "payments_ollama_training.jsonl"

usa = ["USA"]
non_usa = ["India", "China", "Turkey", "Mexico", "Germany", "France", "UK", "Brazil", "Canada", "Spain"]

def classify(origin_country, amount):
    if origin_country == "USA":
        if amount < 50:
            return "auto-approved"
        else:
            return "challenged"
    else:
        if amount < 50:
            return "rejected"
        else:
            return "fraud"

records = []

for i in range(500):
    # Randomly choose USA or non-USA
    if random.random() < 0.5:
        country = random.choice(usa)
    else:
        country = random.choice(non_usa)

    # Random amount between 1 and 200
    amount = round(random.uniform(1, 200), 2)

    label = classify(country, amount)

    record = {
        "messages": [
            {
                "role": "system",
                "content": "You are a payment fraud detection system. Classify transactions strictly based on country of origin and amount."
            },
            {
                "role": "user",
                "content": f"Transaction from {country} with amount {amount} USD."
            },
            {
                "role": "assistant",
                "content": label
            }
        ]
    }

    records.append(record)

# Write JSONL (important for Ollama)
with open(OUTPUT_FILE, "w") as f:
    for r in records:
        f.write(json.dumps(r) + "\n")

print(f"Generated 500 records in {OUTPUT_FILE}")
