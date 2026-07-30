import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/superstore.csv", encoding="latin1")

print("="*50)
print("DATASET SHAPE")
print("="*50)
print(df.shape)

print("\n" + "="*50)
print("COLUMN NAMES")
print("="*50)
print(df.columns.tolist())

print("\n" + "="*50)
print("FIRST 5 ROWS")
print("="*50)
print(df.head())

print("\n" + "="*50)
print("DATASET INFO")
print("="*50)
df.info()

print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)
print(df.isnull().sum())

print("\n" + "="*50)
print("DUPLICATE RECORDS")
print("="*50)
print(df.duplicated().sum())