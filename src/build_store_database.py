"""Build a small local SQLite database from CSV files."""

from pathlib import Path
import sqlite3

import pandas as pd


def load_csv_as_df(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    raw_dir = project_root / "data" / "raw"
    processed_dir = project_root / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    db_path = processed_dir / "park_vintage.db"

    inventory = load_csv_as_df(raw_dir / "inventory.csv")
    sales = load_csv_as_df(raw_dir / "sales.csv")
    products = load_csv_as_df(raw_dir / "products.csv")
    customers = load_csv_as_df(raw_dir / "customers.csv")

    conn = sqlite3.connect(db_path)
    try:
        inventory.to_sql("inventory", conn, if_exists="replace", index=False)
        sales.to_sql("sales", conn, if_exists="replace", index=False)
        products.to_sql("products", conn, if_exists="replace", index=False)
        customers.to_sql("customers", conn, if_exists="replace", index=False)

        print(f"✅ Wrote database: {db_path}")
        print(f"inventory rows: {len(inventory)}")
        print(f"sales rows: {len(sales)}")
        print(f"products rows: {len(products)}")
        print(f"customers rows: {len(customers)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
