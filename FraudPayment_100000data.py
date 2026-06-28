import json
import random

OUTPUT_FILE = "fraud_score_training_100000.json"

merchants = [
    "Amazon", "Walmart", "Target", "Apple",
    "BestBuy", "Costco", "Ebay", "Nike",
    "Adidas", "HomeDepot"
]

devices = ["iPhone", "Android", "Windows-PC", "MacBook", "iPad"]

countries = [
    "USA", "India", "China", "Turkey", "Mexico",
    "Germany", "France", "UK", "Brazil", "Canada"
]

def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def classify(fraud_score):
    if 0 <= fraud_score <= 30:
        return "Auto Approve"
    elif 31 <= fraud_score <= 50:
        return "Approve + Flag"
    elif 51 <= fraud_score <= 70:
        return "Step-Up Auth (SMS OTP or Biometric)"
    elif 71 <= fraud_score <= 85:
        return "Investigator Review"
    elif 86 <= fraud_score <= 100:
        return "Auto Decline"

records = []

for i in range(100000):

    fraud_score = random.randint(0, 100)
    decision = classify(fraud_score)

    amount = round(random.uniform(1, 500), 2)
    merchant = random.choice(merchants)
    device = random.choice(devices)
    country = random.choice(countries)
    ip = random_ip()

    html_input = f"""Classify the payment transaction based on Fraud Score:
<div class='transaction'>
<h2>Transaction TXN{10000 + i}</h2>
<span class='origin_country'>{country}</span>
<span class='amount'>${amount}</span>
<span class='merchant'>{merchant}</span>
<span class='device'>{device}</span>
<span class='ip_address'>{ip}</span>
<span class='fraud_score'>{fraud_score}</span>
</div>"""

    record = {
        "input": html_input,
        "output": {
            "status": decision
        }
    }

    records.append(record)

with open(OUTPUT_FILE, "w") as f:
    json.dump(records, f, indent=2)

print(f"Successfully generated 100000 records in {OUTPUT_FILE}")
