# Week-3-Introduction-to-Data-Analysis---Working-with-Real-Data
Introduction to Data Analysis - Working with Real Data
Sales Data Analysis Report
1. Introduction

This project analyzes sample sales data using Python and the Pandas library. The purpose is to understand sales performance, clean the dataset, and identify the highest-revenue product.

2. Dataset Overview
Source: sales_data.csv
Original records: 13
Records after duplicate removal: 12
Columns: Order_ID, Product, Quantity, Unit_Price, Total_Sales
3. Data Cleaning
Removed duplicate orders using Order_ID.
Filled missing sales values using Quantity × Unit_Price.
Removed rows with missing critical data.
Excluded records with negative quantities, prices, or sales.
4. Key Findings
Metric	Result
Total revenue	₹3,30,300.00
Valid orders	12
Total units sold	61
Average order value	₹27,525.00
Highest-revenue product	Laptop
Laptop revenue	₹2,25,000.00
5. Revenue by Product
Product	Revenue
Laptop	₹2,25,000.00
Monitor	₹60,000.00
Headphones	₹18,000.00
Mouse	₹16,500.00
Keyboard	₹10,800.00
6. Insights
Laptops generated the highest revenue.
Monitors were the second-highest revenue contributor.
Duplicate and incomplete records were addressed before calculating the metrics.
The average order value was ₹27,525.00.
7. Conclusion

This project demonstrates how Pandas can load, explore, clean, and analyze CSV data. The results identify the products generating the most revenue and provide a useful summary of overall sales performance.

Note: The dataset is sample data created for learning purposes and does not represent actual business transactions.
