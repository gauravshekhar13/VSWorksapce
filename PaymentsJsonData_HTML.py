import json
import random

OUTPUT_FILE = "payments_extraction_style_500.json"

usa = ["USA"]
non_usa = [
    "India", "China", "Turkey", "Mexico",
    "Germany", "France", "UK", "Brazil",
    "Spain", "Canada", "Italy"
]

merchants = [
    "Amazon", "Walmart", "Target", "Apple",
    "BestBuy", "Costco", "Ebay", "Nike",
    "Adidas", "HomeDepot"
]

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
    score = random.randint(10, 40)

    if origin_country != "USA":
        score += 30

    if amount > 50:
        score += 20

    return min(score, 100)

records = []

for i in range(500):

    # Random country selection
    country = random.choice(usa + non_usa)
    amount = round(random.uniform(1, 200), 2)

    merchant = random.choice(merchants)
    ip = random_ip()
    device = random.choice(devices)
    risk_score = calculate_risk_score(country, amount)

    status = classify(country, amount)

    # HTML-style structured input (like your product example)
    input_text = f"""Classify the payment transaction:
<div class='transaction'>
<span class='transaction_id'>TXN{10000 + i}</span>
<span class='origin_country'>{country}</span>
<span class='amount'>${amount}</span>
<span class='currency'>USD</span>
<span class='merchant'>{merchant}</span>
<span class='ip_address'>{ip}</span>
<span class='device'>{device}</span>
<span class='risk_score'>{risk_score}</span>
</div>"""

    record = {
        "input": input_text,
        "output": {
            "status": status
        }
    }

    records.append(record)

with open(OUTPUT_FILE, "w") as f:
    json.dump(records, f, indent=2)

print(f"Generated 500 records in {OUTPUT_FILE}")
