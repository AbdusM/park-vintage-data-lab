"""Create a monthly sales summary and simple category/channel metrics."""

from pathlib import Path

import pandas as pd


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    raw_dir = project_root / "data" / "raw"
    processed_dir = project_root / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    inventory = pd.read_csv(raw_dir / "inventory.csv")
    sales = pd.read_csv(raw_dir / "sales.csv")

    sales["sale_date"] = pd.to_datetime(sales["sale_date"])
    merged = sales.merge(inventory[["item_id", "category", "product_name", "cost", "list_price"]], on="item_id", how="left")

    merged["revenue"] = merged["sale_price"]
    merged["profit"] = merged["sale_price"] - merged["cost"]
    merged["profit_margin_pct"] = (merged["profit"] / merged["cost"]).replace([float("inf"), -float("inf")], 0) * 100

    merged["month"] = merged["sale_date"].dt.to_period("M").astype(str)
    monthly = (
        merged.groupby("month")[["revenue", "profit"]]
        .sum(numeric_only=True)
        .round(2)
        .reset_index()
    )
    monthly.to_csv(processed_dir / "monthly_sales_summary.csv", index=False)

    print("Total revenue:", round(merged["revenue"].sum(), 2))
    print("Total profit:", round(merged["profit"].sum(), 2))
    top_category = merged.groupby("category")["revenue"].sum().sort_values(ascending=False).head(3)
    top_channel = merged.groupby("channel")["revenue"].sum().sort_values(ascending=False)

    print("Top categories:\n", top_category)
    print("Top channel:\n", top_channel.head(1))
    print(f"Saved: {processed_dir / 'monthly_sales_summary.csv'}")


if __name__ == "__main__":
    main()
