import random
from locust import HttpUser, task, between

class FraudGuardUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def health_check(self):
        self.client.get("/health")

    @task(3)
    def predict_fraud(self):
        # Sample payload based on schemas.py
        payload = {
            "TransactionAmt": random.uniform(10.0, 5000.0),
            "ProductCD": random.choice(["W", "H", "C", "S", "R"]),
            "card1": random.randint(1000, 20000),
            "card2": random.uniform(100.0, 600.0),
            "card3": 150.0,
            "card4": random.choice(["visa", "mastercard"]),
            "card5": 117.0,
            "card6": random.choice(["debit", "credit"]),
            "addr1": random.uniform(100.0, 500.0),
            "dist1": random.uniform(1.0, 100.0),
            "P_emaildomain": "gmail.com",
            "C1": random.uniform(1.0, 10.0),
            "C2": random.uniform(1.0, 10.0),
            "V1": 1.0, "V2": 1.0, "V3": 1.0, "V4": 1.0, "V5": 1.0,
            "V6": 1.0, "V7": 1.0, "V8": 1.0, "V9": 1.0, "V10": 1.0,
            "V11": 1.0, "V12": 1.0, "V13": 1.0, "V14": 1.0, "V15": 1.0,
            "V16": 1.0, "V17": 1.0, "V18": 1.0, "V19": 1.0, "V20": 1.0
        }
        self.client.post("/predict", json=payload)
