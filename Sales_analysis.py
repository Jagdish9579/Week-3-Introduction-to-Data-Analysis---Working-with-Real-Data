
# Week 3 Project: Sales Data Analysis
# Analyze sales data using the pandas library.

import pandas as pd


def main():
    # Step 1: Load the CSV dataset.
    try:
        df = pd.read_csv("sales_data.csv")
    except FileNotFoundError:
        print("Error: sales_data.csv was not found.")
        print("Place the CSV file in the same folder as this script.")
        return

    # Step 2: Display the original dataset information.
    print("=" * 55)
    print("             SALES DATA ANALYSIS")
    print("=" * 55)

    print("\nFirst five rows:")
    print(df.head())

    print("\nDataset shape (rows, columns):", df.shape)
    print("\nColumn names:", df.columns.tolist())
    print("\nData types:")
    print(df.dtypes)

    # Step 3: Check for missing values.
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    # Step 4: Remove duplicate orders.
    df = df.drop_duplicates(subset="Order_ID", keep="first")

    # Step 5: Convert numeric columns safely.
    numeric_columns = ["Quantity", "Unit_Price", "Total_Sales"]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Step 6: Fill missing sales using quantity * unit price.
    calculated_sales = df["Quantity"] * df["Unit_Price"]
    df["Total_Sales"] = df["Total_Sales"].fillna(calculated_sales)

    # Remove rows that still have missing critical data.
    df = df.dropna(
        subset=["Order_ID", "Product", "Quantity",
                "Unit_Price", "Total_Sales"]
    )

    # Exclude invalid sales values.
    df = df[
        (df["Quantity"] >= 0)
        & (df["Unit_Price"] >= 0)
        & (df["Total_Sales"] >= 0)
    ].copy()

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    # Step 7: Calculate key sales metrics.
    total_revenue = df["Total_Sales"].sum()
    total_units = df["Quantity"].sum()
    average_order_value = df["Total_Sales"].mean()

    # Find the product with the highest total revenue.
    product_revenue = df.groupby("Product")["Total_Sales"].sum()
    best_product = product_revenue.idxmax()
    best_product_revenue = product_revenue.max()

    # Find the highest-value order.
    highest_order = df.loc[df["Total_Sales"].idxmax()]

    # Step 8: Display the cleaned data and report.
    print("\nCleaned dataset:")
    print(df.to_string(index=False))

    print("\n" + "=" * 55)
    print("                 SALES REPORT")
    print("=" * 55)
    print(f"Valid orders: {len(df)}")
    print(f"Total revenue: ₹{total_revenue:,.2f}")
    print(f"Total units sold: {total_units:,.0f}")
    print(f"Average order value: ₹{average_order_value:,.2f}")
    print(f"Best product by revenue: {best_product}")
    print(f"Revenue from best product: ₹{best_product_revenue:,.2f}")
    print(
        f"Highest-value order: {int(highest_order['Order_ID'])} "
        f"(₹{highest_order['Total_Sales']:,.2f})"
    )

    print("\nRevenue by product:")
    print(product_revenue.sort_values(ascending=False).to_string())

    # Step 9: Save a reusable report.
    with open("analysis_report.md", "w", encoding="utf-8") as file:
        file.write("# Sales Data Analysis Report\n\n")
        file.write("## Summary Metrics\n\n")
        file.write(f"- Valid orders: {len(df)}\n")
        file.write(f"- Total revenue: ₹{total_revenue:,.2f}\n")
        file.write(f"- Total units sold: {total_units:,.0f}\n")
        file.write(
            f"- Average order value: ₹{average_order_value:,.2f}\n"
        )
        file.write(f"- Best product by revenue: {best_product}\n")
        file.write(
            f"- Revenue from best product: ₹{best_product_revenue:,.2f}\n"
        )
        file.write(
            f"- Highest-value order: {int(highest_order['Order_ID'])} "
            f"(₹{highest_order['Total_Sales']:,.2f})\n"
        )
        file.write("\n## Revenue by Product\n\n")
        file.write("| Product | Revenue |\n")
        file.write("|---|---:|\n")

        for product, revenue in product_revenue.sort_values(
            ascending=False
        ).items():
            file.write(f"| {product} | ₹{revenue:,.2f} |\n")

        file.write("\n## Data Cleaning\n\n")
        file.write("- Removed duplicate Order_ID entries.\n")
        file.write("- Filled missing sales from quantity × unit price.\n")
        file.write("- Removed rows with missing critical values.\n")
        file.write("- Excluded negative quantities, prices, and sales.\n")

    print("\nReport saved to analysis_report.md")


if __name__ == "__main__":
    main()
