"""
Sales Trend Visualization
--------------------------
Loads sales transaction data and produces a set of visualizations
that reveal trends over time, by category, by region, and by weekday.

Output charts are saved as PNG files in the 'outputs' folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 110

DATA_PATH = "data/sales_data.csv"
OUT_DIR = "outputs"

# ---------------------------------------------------------
# 1. Load and prepare data
# ---------------------------------------------------------
df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)
df["Year"] = df["Date"].dt.year
df["Weekday"] = df["Date"].dt.day_name()

print("Dataset shape:", df.shape)
print(df.head())
print("\nSummary stats:\n", df["Revenue"].describe())

# ---------------------------------------------------------
# 2. Monthly Revenue Trend (Line Chart)
# ---------------------------------------------------------
monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()

plt.figure(figsize=(12, 5))
plt.plot(monthly_revenue["Month"], monthly_revenue["Revenue"], marker="o", color="#2E86AB")
plt.title("Monthly Sales Revenue Trend (2022-2024)", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Total Revenue ($)")
plt.xticks(rotation=75, fontsize=8)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/01_monthly_revenue_trend.png")
plt.close()

# ---------------------------------------------------------
# 3. Yearly Revenue Comparison (Bar Chart)
# ---------------------------------------------------------
yearly_revenue = df.groupby("Year")["Revenue"].sum().reset_index()

plt.figure(figsize=(7, 5))
sns.barplot(data=yearly_revenue, x="Year", y="Revenue", hue="Year", palette="Blues_d", legend=False)
plt.title("Total Revenue by Year", fontsize=14, fontweight="bold")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/02_yearly_revenue.png")
plt.close()

# ---------------------------------------------------------
# 4. Revenue by Product Category (Bar Chart)
# ---------------------------------------------------------
category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=category_revenue, x="Revenue", y="Category", hue="Category", palette="viridis", legend=False)
plt.title("Total Revenue by Product Category", fontsize=14, fontweight="bold")
plt.xlabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/03_revenue_by_category.png")
plt.close()

# ---------------------------------------------------------
# 5. Revenue by Region (Pie Chart)
# ---------------------------------------------------------
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(7, 7))
plt.pie(
    region_revenue,
    labels=region_revenue.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=sns.color_palette("pastel"),
)
plt.title("Revenue Share by Region", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/04_revenue_by_region.png")
plt.close()

# ---------------------------------------------------------
# 6. Category Trend Over Time (Multi-line Chart)
# ---------------------------------------------------------
cat_month = df.groupby(["Month", "Category"])["Revenue"].sum().reset_index()
pivot_cat = cat_month.pivot(index="Month", columns="Category", values="Revenue").fillna(0)

plt.figure(figsize=(13, 6))
for col in pivot_cat.columns:
    plt.plot(pivot_cat.index, pivot_cat[col], marker="o", markersize=3, label=col)
plt.title("Monthly Revenue Trend by Category", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=75, fontsize=7)
plt.legend(title="Category", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/05_category_trend_over_time.png")
plt.close()

# ---------------------------------------------------------
# 7. Sales by Day of Week (Bar Chart)
# ---------------------------------------------------------
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_revenue = df.groupby("Weekday")["Revenue"].sum().reindex(weekday_order).reset_index()

plt.figure(figsize=(9, 5))
sns.barplot(data=weekday_revenue, x="Weekday", y="Revenue", hue="Weekday", palette="magma", legend=False)
plt.title("Total Revenue by Day of Week", fontsize=14, fontweight="bold")
plt.ylabel("Total Revenue ($)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/06_revenue_by_weekday.png")
plt.close()

# ---------------------------------------------------------
# 8. Heatmap: Category vs Region Revenue
# ---------------------------------------------------------
heat_data = df.pivot_table(values="Revenue", index="Category", columns="Region", aggfunc="sum")

plt.figure(figsize=(8, 6))
sns.heatmap(heat_data, annot=True, fmt=".0f", cmap="YlGnBu", linewidths=0.5)
plt.title("Revenue Heatmap: Category vs Region", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/07_category_region_heatmap.png")
plt.close()

# ---------------------------------------------------------
# 9. Save a summary report (text)
# ---------------------------------------------------------
with open(f"{OUT_DIR}/summary_report.txt", "w") as f:
    f.write("SALES TREND VISUALIZATION - SUMMARY REPORT\n")
    f.write("=" * 45 + "\n\n")
    f.write(f"Total records analyzed: {len(df):,}\n")
    f.write(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()}\n")
    f.write(f"Total revenue: ${df['Revenue'].sum():,.2f}\n")
    f.write(f"Average transaction value: ${df['Revenue'].mean():,.2f}\n\n")

    f.write("Revenue by Year:\n")
    f.write(yearly_revenue.to_string(index=False) + "\n\n")

    f.write("Revenue by Category:\n")
    f.write(category_revenue.to_string(index=False) + "\n\n")

    f.write("Revenue by Region:\n")
    f.write(region_revenue.to_string() + "\n\n")

    best_month = monthly_revenue.loc[monthly_revenue["Revenue"].idxmax()]
    f.write(f"Best performing month: {best_month['Month']} (${best_month['Revenue']:,.2f})\n")

    best_weekday = weekday_revenue.loc[weekday_revenue["Revenue"].idxmax()]
    f.write(f"Best performing weekday: {best_weekday['Weekday']} (${best_weekday['Revenue']:,.2f})\n")

print("\nAll charts and summary report saved to the 'outputs' folder.")
