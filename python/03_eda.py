import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(
    "../data/cleaned/superstore_cleaned.csv",
    parse_dates=["Order Date", "Ship Date"]
)

# -----------------------------
# Create output folder
# -----------------------------
os.makedirs("../dashboard_images", exist_ok=True)

# -----------------------------
# KPI SUMMARY
# -----------------------------
print("="*60)
print("KPI SUMMARY")
print("="*60)

print(f"Total Sales       : ₹{df['Sales'].sum():,.2f}")
print(f"Total Profit      : ₹{df['Profit'].sum():,.2f}")
print(f"Total Orders      : {df['Order ID'].nunique()}")
print(f"Total Customers   : {df['Customer ID'].nunique()}")
print(f"Average Order     : ₹{df['Sales'].mean():,.2f}")

# ===========================================
# MONTHLY SALES TREND
# ===========================================

monthly_sales = (
    df.set_index("Order Date")
      .resample("ME")["Sales"]
      .sum()
)

plt.figure(figsize=(14,6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend", fontsize=16)

plt.xlabel("Date")

plt.ylabel("Sales")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../dashboard_images/monthly_sales_trend.png",
    dpi=300
)

plt.show()

print("✔ Monthly Sales Trend Saved")

# ===========================================
# MONTHLY PROFIT TREND
# ===========================================

monthly_profit = (
    df.set_index("Order Date")
      .resample("ME")["Profit"]
      .sum()
)

plt.figure(figsize=(14,6))

plt.plot(
    monthly_profit.index,
    monthly_profit.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Profit Trend", fontsize=16)

plt.xlabel("Date")

plt.ylabel("Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../dashboard_images/monthly_profit_trend.png",
    dpi=300
)

plt.show()

print("✔ Monthly Profit Trend Saved")

# ===========================================
# SALES BY CATEGORY
# ===========================================

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

category_sales.plot(
    kind="bar"
)

plt.title("Sales by Category", fontsize=16)

plt.xlabel("Category")

plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "../dashboard_images/sales_by_category.png",
    dpi=300
)

plt.show()

print("✔ Sales by Category Saved")

# ===========================================
# PROFIT BY CATEGORY
# ===========================================

category_profit = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

category_profit.plot(
    kind="bar"
)

plt.title("Profit by Category", fontsize=16)

plt.xlabel("Category")

plt.ylabel("Profit")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "../dashboard_images/profit_by_category.png",
    dpi=300
)

plt.show()

print("✔ Profit by Category Saved")

# ===========================================
# SALES BY REGION
# ===========================================

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

region_sales.plot(
    kind="bar"
)

plt.title("Sales by Region", fontsize=16)

plt.xlabel("Region")

plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "../dashboard_images/sales_by_region.png",
    dpi=300
)

plt.show()

print("✔ Sales by Region Saved")

# ===========================================
# PROFIT BY REGION
# ===========================================

region_profit = (
    df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

region_profit.plot(
    kind="bar"
)

plt.title("Profit by Region", fontsize=16)

plt.xlabel("Region")

plt.ylabel("Profit")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "../dashboard_images/profit_by_region.png",
    dpi=300
)

plt.show()

print("✔ Profit by Region Saved")

# ===========================================
# TOP 10 PRODUCTS BY SALES
# ===========================================

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))

top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales", fontsize=16)
plt.xlabel("Product Name")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "../dashboard_images/top10_products.png",
    dpi=300
)

plt.show()

print("✔ Top 10 Products Saved")

# ===========================================
# TOP 10 CUSTOMERS BY SALES
# ===========================================

top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))

top_customers.plot(kind="bar")

plt.title("Top 10 Customers by Sales", fontsize=16)
plt.xlabel("Customer Name")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "../dashboard_images/top10_customers.png",
    dpi=300
)

plt.show()

print("✔ Top 10 Customers Saved")

# ===========================================
# SALES BY SEGMENT
# ===========================================

segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

segment_sales.plot(kind="bar")

plt.title("Sales by Segment", fontsize=16)
plt.xlabel("Segment")
plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "../dashboard_images/sales_by_segment.png",
    dpi=300
)

plt.show()

print("✔ Sales by Segment Saved")

# ===========================================
# DISCOUNT VS PROFIT
# ===========================================

plt.figure(figsize=(8,6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit", fontsize=16)
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../dashboard_images/discount_vs_profit.png",
    dpi=300
)

plt.show()

print("✔ Discount vs Profit Saved")

# ===========================================
# TOP 10 STATES BY SALES
# ===========================================

state_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))

state_sales.plot(kind="bar")

plt.title("Top 10 States by Sales", fontsize=16)
plt.xlabel("State")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "../dashboard_images/top10_states_sales.png",
    dpi=300
)

plt.show()

print("✔ Top 10 States by Sales Saved")

# ===========================================
# TOP 10 LOSS-MAKING PRODUCTS
# ===========================================

loss_products = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values()
      .head(10)
)

plt.figure(figsize=(12,6))

loss_products.plot(kind="bar")

plt.title("Top 10 Loss-Making Products", fontsize=16)
plt.xlabel("Product Name")
plt.ylabel("Profit")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "../dashboard_images/top10_loss_products.png",
    dpi=300
)

plt.show()

print("✔ Top 10 Loss-Making Products Saved")