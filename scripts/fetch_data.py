import pandas as pd

data = {
    "name": ["Ankita", "Rahul"],
    "salary": [50000, 60000]
}

df = pd.DataFrame(data)

df.to_csv("data/employees.csv", index=False)

print("CSV created")