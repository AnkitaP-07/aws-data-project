import pandas as pd
import os

data = {
    "name": ["Ankita", "Rahul", "Priya"],
    "salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)

df.to_csv("data/employees.csv", index=False)

print("CSV created successfully")