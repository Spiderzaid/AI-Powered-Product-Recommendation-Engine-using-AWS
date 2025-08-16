
import csv, random, time, os
from datetime import datetime, timedelta
random.seed(7)

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE, ".."))

items = [
    ("I100", "Audio"),
    ("I101", "TV"),
    ("I102", "Accessories"),
    ("I103", "Outdoors"),
]
users = [f"U{str(i).zfill(3)}" for i in range(1, 21)]
events = ["view", "add_to_cart", "purchase"]

def write_interactions():
    path = os.path.join(DATA_DIR, "sample_interactions.csv")
    now = datetime.utcnow()
    rows = []
    for _ in range(300):
        u = random.choice(users)
        it, cat = random.choice(items)
        et = random.choices(events, weights=[0.8, 0.15, 0.05])[0]
        ts = now - timedelta(minutes=random.randint(0, 60*24*7))
        rows.append((u, it, et, ts.isoformat()))

    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["user_id","item_id","event_type","ts"])
        w.writerows(rows)
    print(f"Wrote {path} ({len(rows)} rows)")

if __name__ == "__main__":
    write_interactions()
