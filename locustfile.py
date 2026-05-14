import random
from locust import HttpUser, task, between

class FraudGuardUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def health_check(self):
        self.client.get("/health")

    @task(5)
    def predict_fraud(self):
        # Precise payload matching TransactionRequest in app/schemas.py
        payload = {
            "TransactionAmt": random.uniform(10.0, 500.0),
            "TransactionDT": random.randint(86400, 86400 * 30),
            "ProductCD": random.choice(["W", "H", "C", "S", "R"]),
            "card1": float(random.randint(1000, 20000)),
            "card2": float(random.randint(100, 600)),
            "card3": 150.0,
            "card4": random.choice(["visa", "mastercard"]),
            "card5": 117.0,
            "card6": random.choice(["debit", "credit"]),
            "addr1": 315.0,
            "addr2": 87.0,
            "dist1": random.uniform(1.0, 100.0),
            "P_emaildomain": "gmail.com",
            "C1": 1.0, "C2": 1.0, "C3": 0.0, "C4": 0.0, "C5": 0.0,
            "C6": 1.0, "C7": 0.0, "C8": 0.0, "C9": 1.0, "C10": 0.0,
            "C11": 1.0, "C12": 0.0, "C13": 1.0, "C14": 1.0,
            "V1": 1.0, "V2": 1.0, "V3": 1.0, "V4": 1.0, "V5": 1.0,
            "V12": 1.0, "V13": 1.0, "V14": 1.0, "V36": 0.0, "V37": 1.0,
            "V38": 1.0, "V54": 1.0, "V55": 1.0, "V56": 1.0, "V75": 1.0,
            "V76": 1.0, "V77": 1.0, "V78": 1.0, "V282": 1.0, "V283": 1.0
        }
        self.client.post("/predict", json=payload)
