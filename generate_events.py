
import json
import random
from datetime import datetime, timedelta


random.seed(42)

signatures = [
    "SSH Brute Force Attempt",
    "Port Scan Detected",
    "SQL Injection Attempt",
    "Suspicious DNS Query",
    "XSS Attempt",
    "Malware Communication"
]

weights = [30, 20, 15, 15, 10, 10]

severity_levels = {
    "SSH Brute Force Attempt": "High",
    "Port Scan Detected": "Medium",
    "SQL Injection Attempt": "Critical",
    "Suspicious DNS Query": "Low",
    "XSS Attempt": "High",
    "Malware Communication": "Critical"
}

events = []

start_time = datetime(2026, 11, 24, 9, 0, 0)

for i in range(100):
    signature = random.choices(
        signatures,
        weights=weights,
        k=1
    )[0]

    event = {
        "timestamp": (
            start_time + timedelta(minutes=i * 3)
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "src_ip": f"192.168.1.{random.randint(100, 150)}",
        "dest_ip": f"10.0.0.{random.randint(1, 50)}",
        "signature": signature,
        "severity": severity_levels[signature]
    }

    events.append(event)

with open("events.json", "w", encoding="utf-8") as file:
    json.dump(events, file, ensure_ascii=False, indent=4)

print(f"Создано событий: {len(events)}")
print("Файл events.json успешно обновлён.")
