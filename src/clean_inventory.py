"""Clean Park Vintage inventory data for beginners.

This script reads raw inventory data, fixes simple data issues, and calculates
margin columns used in later analysis.
"""

from pathlib import Path

import pandas as pd


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    raw_path = project_root / "data" / "raw" / "inventory.csv"
    output_dir = project_root / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "cleaned_inventory.csv"

    inventory = pd.read_csv(raw_path)

    # Fill simple missing values so exercises can continue without hard failures.
    inventory["brand"] = inventory["brand"].fillna("Unknown")
    inventory["size"] = inventory["size"].fillna("Unknown")
    inventory["status"] = inventory["status"].fillna("In Stock")
    inventory["category"] = inventory["category"].fillna("Uncategorized")

    # Ensure numeric math values are usable.
    inventory["cost"] = pd.to_numeric(inventory["cost"], errors="coerce").fillna(0)
    inventory["list_price"] = pd.to_numeric(inventory["list_price"], errors="coerce").fillna(0)

    # Add beginner-friendly business columns.
    inventory["margin"] = inventory["list_price"] - inventory["cost"]
    inventory["margin_percent"] = (inventory["margin"] / inventory["cost"]).replace([float("inf"), -float("inf")], 0) * 100
    inventory["margin_percent"] = inventory["margin_percent"].fillna(0).round(2)

    inventory.to_csv(output_path, index=False)
    print(f"✅ Saved cleaned inventory to {output_path}")
    print(f"Rows: {len(inventory)}")


if __name__ == "__main__":
    main()
