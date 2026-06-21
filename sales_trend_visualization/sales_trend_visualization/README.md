# 📈 Sales Trend Visualization

A data analytics project that analyzes retail sales transaction data and visualizes trends across time, product categories, regions, and weekdays. Built as part of a Data Analytics internship project submission for **CodeTech IT Solutions**.

---

## 📌 Project Overview

This project explores a simulated multi-year retail sales dataset (2022–2024) to uncover patterns in revenue performance. The goal is to demonstrate core data analytics skills: data cleaning, aggregation, trend analysis, and visualization using Python.

**Key questions answered:**
- How does total revenue trend month-over-month and year-over-year?
- Which product categories generate the most revenue?
- How is revenue distributed across regions?
- Are there seasonal or weekday sales patterns?
- Which category performs best in each region?

---

## 🗂️ Project Structure

```
sales_trend_visualization/
│
├── data/
│   └── sales_data.csv              # Transaction-level sales dataset
│
├── outputs/
│   ├── 01_monthly_revenue_trend.png
│   ├── 02_yearly_revenue.png
│   ├── 03_revenue_by_category.png
│   ├── 04_revenue_by_region.png
│   ├── 05_category_trend_over_time.png
│   ├── 06_revenue_by_weekday.png
│   ├── 07_category_region_heatmap.png
│   └── summary_report.txt          # Auto-generated text summary
│
├── generate_data.py                # Script to generate the synthetic dataset
├── sales_trend_analysis.py         # Main analysis & visualization script
├── requirements.txt
└── README.md
```

---

## 🧰 Tech Stack

- **Python 3**
- **Pandas** — data manipulation & aggregation
- **Matplotlib** — chart rendering
- **Seaborn** — statistical visualization styling

---

## 📊 Dataset

The dataset (`data/sales_data.csv`) contains ~16,500 transaction records with the following fields:

| Column | Description |
|---|---|
| `Date` | Date of transaction |
| `Category` | Product category (Electronics, Clothing, Home & Kitchen, Sports, Beauty) |
| `Region` | Sales region (North, South, East, West) |
| `Quantity` | Units sold in the transaction |
| `UnitPrice` | Price per unit ($) |
| `Revenue` | Total transaction revenue ($) |

> Note: The dataset is synthetically generated with realistic seasonal patterns (holiday spikes in Nov–Dec, weekend boosts, year-over-year growth) to simulate real-world retail behavior. You can replace `data/sales_data.csv` with your own real dataset — the analysis script will work as long as the column names match.

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/sales-trend-visualization.git
   cd sales-trend-visualization
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Regenerate the dataset**
   ```bash
   python generate_data.py
   ```

4. **Run the analysis**
   ```bash
   python sales_trend_analysis.py
   ```

5. Check the `outputs/` folder for all generated charts and the summary report.

---

## 📈 Sample Visualizations

| Chart | Insight |
|---|---|
| Monthly Revenue Trend | Reveals overall growth trajectory and seasonal spikes |
| Yearly Revenue Comparison | Shows year-over-year business growth |
| Revenue by Category | Identifies top-performing product lines |
| Revenue by Region (Pie) | Shows regional revenue contribution |
| Category Trend Over Time | Tracks how each category performs across months |
| Revenue by Weekday | Highlights peak shopping days |
| Category–Region Heatmap | Pinpoints which category sells best in which region |

---

## 🔍 Key Insights (from this dataset)

- Revenue consistently peaks in **November–December**, reflecting holiday season demand.
- **Electronics** is the top-grossing category overall.
- **Weekends** generate noticeably higher revenue than weekdays.
- Revenue shows a steady **year-over-year upward trend** (~12% growth simulated annually).
- Regional performance is fairly balanced, with slight variation by category.

---

## 🚀 Future Improvements

- Add interactive dashboards using Plotly/Dash or Power BI
- Incorporate forecasting (e.g., ARIMA, Prophet) for future sales prediction
- Connect to a live database or API for real-time analysis
- Add customer segmentation analysis

---

## 👤 Author

Submitted as part of a Data Analytics Internship project at **CodeTech IT Solutions**.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
