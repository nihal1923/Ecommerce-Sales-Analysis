from pathlib import Path

import pandas as pd


# Project paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

INPUT_FILE = PROJECT_DIR / "data" / "cleaned" / "superstore_cleaned.csv"
OUTPUT_FILE = PROJECT_DIR / "data" / "cleaned" / "superstore_sql.csv"


def main() -> None:
    """Create a clean CSV file for importing into MySQL."""

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned dataset was not found:\n{INPUT_FILE}"
        )

    df = pd.read_csv(
        INPUT_FILE,
        parse_dates=["Order Date", "Ship Date"]
    )

    # Keep the original 21 business columns
    sql_columns = [
        "Row ID",
        "Order ID",
        "Order Date",
        "Ship Date",
        "Ship Mode",
        "Customer ID",
        "Customer Name",
        "Segment",
        "Country",
        "City",
        "State",
        "Postal Code",
        "Region",
        "Product ID",
        "Category",
        "Sub-Category",
        "Product Name",
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    missing_columns = [
        column for column in sql_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    df = df[sql_columns].copy()

    # Rename columns into SQL-friendly snake_case
    df.columns = [
        "row_id",
        "order_id",
        "order_date",
        "ship_date",
        "ship_mode",
        "customer_id",
        "customer_name",
        "segment",
        "country",
        "city",
        "state",
        "postal_code",
        "region",
        "product_id",
        "category",
        "sub_category",
        "product_name",
        "sales",
        "quantity",
        "discount",
        "profit"
    ]

    # MySQL-friendly date format
    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")
    df["ship_date"] = df["ship_date"].dt.strftime("%Y-%m-%d")

    # Postal codes are identifiers, not values used in calculations
    df["postal_code"] = pd.to_numeric(
        df["postal_code"],
        errors="coerce"
    ).astype("Int64")

    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )

    print("=" * 60)
    print("MYSQL EXPORT COMPLETED")
    print("=" * 60)
    print(f"Rows exported    : {len(df)}")
    print(f"Columns exported : {len(df.columns)}")
    print(f"Output file      : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()