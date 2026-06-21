import pandas as pd
import numpy as np

np.random.seed(42)

start_date = "2022-01-01"
end_date = "2024-12-31"
dates = pd.date_range(start_date, end_date, freq="D")

categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty"]
regions = ["North", "South", "East", "West"]

rows = []
for date in dates:
    # seasonal effect (higher sales in Nov-Dec, dip in Feb)
    month = date.month
    seasonal_factor = 1.0
    if month in [11, 12]:
        seasonal_factor = 1.6
    elif month == 2:
        seasonal_factor = 0.8
    elif month in [6, 7]:
        seasonal_factor = 1.15

    # weekly effect (weekends higher)
    weekday_factor = 1.3 if date.dayofweek >= 5 else 1.0

    # mild year-over-year growth trend
    year_factor = 1 + (date.year - 2022) * 0.12

    n_transactions = np.random.poisson(15)
    for _ in range(n_transactions):
        category = np.random.choice(categories, p=[0.28, 0.22, 0.2, 0.15, 0.15])
        region = np.random.choice(regions)
        base_price = {
            "Electronics": 180, "Clothing": 45, "Home & Kitchen": 65,
            "Sports": 55, "Beauty": 30
        }[category]
        quantity = np.random.randint(1, 5)
        unit_price = base_price * np.random.uniform(0.85, 1.2)
        revenue = unit_price * quantity * seasonal_factor * weekday_factor * year_factor
        revenue = round(max(revenue, 5), 2)

        rows.append({
            "Date": date,
            "Category": category,
            "Region": region,
            "Quantity": quantity,
            "UnitPrice": round(unit_price, 2),
            "Revenue": revenue
        })

df = pd.DataFrame(rows)
df.sort_values("Date", inplace=True)
df.to_csv("data/sales_data.csv", index=False)
print(df.shape)
print(df.head())
