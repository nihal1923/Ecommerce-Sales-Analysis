import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/superstore.csv", encoding="latin1")

print("Original Shape:")
print(df.shape)


# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])


# Create time-based columns for analysis

df['Year'] = df['Order Date'].dt.year

df['Month'] = df['Order Date'].dt.month

df['Month Name'] = df['Order Date'].dt.month_name()

df['Quarter'] = df['Order Date'].dt.quarter

df['Day Name'] = df['Order Date'].dt.day_name()


# Create Profit Margin column

df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100


# Check updated dataset

print("\nUpdated Columns:")
print(df.columns.tolist())


print("\nDataset Information:")
print(df.info())


# Save cleaned dataset

df.to_csv("../data/cleaned/superstore_cleaned.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")