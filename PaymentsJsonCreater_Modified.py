import json
import random
import uuid

OUTPUT_FILE = "payments_training_dataset_500.json"

# Countries
usa = ["USA"]
non_usa = [
    "India", "China", "Turkey", "Mexico",
    "Germany", "France", "UK", "Brazil",
    "Spain", "Canada", "Italy"
]

# Merchants
merchants = [
    "Amazon", "Walmart", "Target", "Apple",
    "BestBuy", "Costco", "Ebay", "Nike",
    "Adidas", "HomeDepot"
]

# Devices
devices = ["iPhone", "Android", "Windows-PC", "MacBook", "iPad"]

def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

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

def calculate_risk_score(origin_country, amount):
    base_score = random.randint(10, 40)

    if origin_country != "USA":
        base_score += 30

    if amount > 50:
        base_score += 20

    return min(base_score, 100)

records = []

for i in range(500):

    # Random country
    if random.random() < 0.5:
        country = random.choice(usa)
    else:
        country = random.choice(non_usa)

    amount = round(random.uniform(1, 200), 2)

    label = classify(country, amount)
    risk_score = calculate_risk_score(country, amount)

    record = {
        "instruction": "Classify the payment transaction based on origin country and amount.",
        "input": {
            "transaction_id": f"TXN{10000 + i}",
            "origin_country": country,
            "amount": amount,
            "currency": "USD",
            "merchant": random.choice(merchants),
            "ip_address": random_ip(),
            "device": random.choice(devices),
            "risk_score": risk_score
        },
        "output": label
    }

    records.append(record)

# Write JSON file
with open(OUTPUT_FILE, "w") as f:
    json.dump(records, f, indent=2)

print(f"Successfully generated 500 records in {OUTPUT_FILE}")
