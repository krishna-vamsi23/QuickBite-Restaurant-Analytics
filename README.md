# 🍔 QuickBite Restaurant Analytics Dashboard

## Problem Statement

This project demonstrates an end-to-end Business Intelligence solution for a restaurant chain using **Python, SQL Server, Power BI, and DAX**.

The objective of this project is to analyze restaurant operations by transforming raw business data into meaningful insights through interactive dashboards.

The dashboard enables restaurant management to monitor sales performance, compare store performance, analyze customer behavior, evaluate product sales, and identify business trends for better decision-making.

---

# 🛠 Tools & Technologies Used

- Python
- Pandas
- Faker
- SQL Server
- SQL Server Management Studio (SSMS)
- Power BI Desktop
- DAX
- Git
- GitHub
- Visual Studio Code

---

# Database Design

A relational SQL Server database was designed consisting of six tables.

- Customers
- Orders
- OrderItems
- Products
- Stores
- Employees

Primary Keys and Foreign Keys were implemented to establish relationships between the tables before importing them into Power BI.

---

# Project Workflow

### Step 1

Designed and generated a custom restaurant dataset using **Python (Pandas)** to simulate real-world restaurant operations.

The dataset includes:

- Customers
- Products
- Stores
- Employees
- Orders
- Order Items

Python was used to:

- Generate synthetic business data
- Create realistic customer and sales records
- Simulate restaurant transactions
- Export datasets for SQL Server

## 🐍 Python Dataset Generation

The Python source code is available in the **04_Python** folder.

- [generate_Customers.py](04_Python/generate_Customers.py)
- [generate_employees.py](04_Python/generate_employees.py)
- [generate_orders.py](04_Python/generate_orders.py)
- [generate_orderitems.py](04_Python/generate_orderitems.py)
- [Update_order_totals.py](04_Python/Update_order_totals.py)

---

### Step 2

Created a SQL Server database named **QuickBite**.

---

### Step 3

Imported the generated datasets into SQL Server.

The following tables were created:

- Customers
- Employees
- Stores
- Products
- Orders
- OrderItems

---

### Step 4

Defined appropriate data types for each table.

Examples include:

- NVARCHAR
- INT
- FLOAT
- DATE
- DATETIME2
- TINYINT

---

### Step 5

Performed data validation.

- Verified row counts
- Checked Primary Keys
- Validated Foreign Keys
- Corrected data types
- Removed inconsistencies

---

### Step 6

Created SQL queries to answer business questions.

Examples include:

- Total Revenue
- Total Orders
- Total Customers
- Revenue by Store
- Revenue by Product
- Revenue by Category
- Monthly Revenue Trend
- Top Customers
- Product Performance

---

### Step 7

Imported SQL Server tables into Power BI Desktop.

---

### Step 8

Created relationships between the tables.

Relationships include:

- Customers → Orders
- Stores → Orders
- Employees → Orders
- Orders → OrderItems
- Products → OrderItems

A star schema model was implemented for reporting.

---

### Step 9

Created DAX measures for dashboard analysis.

<details>
<summary>📊 View DAX Measures</summary>

```DAX
Total Revenue =
SUM(Orders[TotalAmount])
```

```DAX
Total Orders =
COUNT(Orders[OrderID])
```

```DAX
Total Customers =
DISTINCTCOUNT(Orders[CustomerID])
```

```DAX
Products Sold =
SUM(OrderItems[Quantity])
```

```DAX
Average Order Value =
DIVIDE([Total Revenue],[Total Orders])
```

</details>

Additional measures include:

- Product Revenue
- Average Selling Price
- Loyalty Members
- Loyalty Percentage
- Customer Revenue
- Store Revenue

---

### Step 10

Built four interactive dashboards in Power BI.

# Dashboard Snapshots

## Executive Dashboard

![Executive Dashboard](Executive_Dashboard.png)

---

## Product Analysis Dashboard

![Product Analysis](Product_Analysis.png)

---

## Store Performance Dashboard

![Store Performance](Store_Performance.png)

---

## Customer Analysis Dashboard

![Customer Analysis](Customer_Analysis.png)

---

# Dashboard Pages

## Executive Dashboard

KPIs

- Total Revenue
- Total Orders
- Total Customers
- Total Products Sold
- Average Order Value

Visualizations

- Monthly Revenue Trend
- Revenue by Store
- Revenue by Category

---

## Product Analysis Dashboard

KPIs

- Product Revenue
- Products Sold
- Average Selling Price

Visualizations

- Top Products by Revenue
- Revenue by Category
- Product Revenue Treemap
- Products Sold by Category

---

## Store Performance Dashboard

KPIs

- Store Revenue
- Total Orders
- Total Customers
- Total Stores

Visualizations

- Revenue by Store
- Orders by Store
- Monthly Revenue Trend
- Revenue Share by Store

---

## Customer Analysis Dashboard

KPIs

- Total Customers
- Loyalty Members
- Loyalty Percentage
- Customer Revenue

Visualizations

- Top Customers
- Customer Distribution
- Revenue by Loyalty Status
- Registration Trend

---

# Business Insights

## [1] Executive Dashboard

- **Total Revenue:** €XXX,XXX
- **Total Orders:** XXX
- **Total Customers:** XXX
- **Total Products Sold:** XXX
- **Average Order Value:** €XX.XX

**Insight**

The Executive Dashboard provides a high-level overview of restaurant performance, allowing management to monitor revenue, customer activity, sales volume, and purchasing trends.

---

## [2] Product Analysis Dashboard

- Highest Revenue Category: **________**
- Best Selling Product: **________**
- Top 10 products contribute the highest percentage of overall revenue.
- Revenue distribution across product categories helps identify profitable menu items.

**Insight**

The dashboard enables management to optimize menu offerings by identifying high-performing and low-performing products.

---

## [3] Store Performance Dashboard

- Best Performing Store: **________**
- Highest Store Revenue: **€________**
- Monthly revenue trends identify peak sales periods.
- Store contribution to overall revenue is visualized through charts.

**Insight**

The dashboard helps compare operational performance across all restaurant locations.

---

## [4] Customer Analysis Dashboard

- Total Customers: **XXX**
- Loyalty Members: **XX%**
- Top Customers identified based on revenue.
- Customer distribution analyzed by city and gender.
- Registration trends show customer growth over time.

**Insight**

Customer analytics help evaluate loyalty programs and identify valuable customer segments.

---

# Skills Demonstrated

## Python

- Pandas
- Faker
- Synthetic Data Generation
- Data Validation
- Data Export

---

## SQL

- Database Design
- Primary Keys
- Foreign Keys
- Joins
- GROUP BY
- ORDER BY
- Aggregate Functions
- Business Queries

---

## Power BI

- Data Modeling
- Interactive Dashboards
- Relationships
- Slicers
- Drill-down Analysis
- Report Navigation

---

## DAX

- SUM
- COUNT
- DISTINCTCOUNT
- SUMX
- DIVIDE
- CALCULATE
- RELATED
- AVERAGE

---

# Key Business Findings

- Identified the highest revenue-generating product category.
- Compared revenue across all restaurant locations.
- Identified top customers based on spending.
- Evaluated customer loyalty participation.
- Analyzed monthly sales trends.
- Compared store performance using interactive dashboards.
- Enabled dynamic filtering using slicers and cross-filtering.

---

# Conclusion

This project demonstrates a complete Business Intelligence workflow, beginning with **custom dataset generation using Python (Pandas)**, followed by **SQL Server database design and querying**, and culminating in **interactive Power BI dashboards using DAX**.

The project showcases practical experience in **Python, Pandas, SQL, ETL, data modeling, DAX, data visualization, dashboard design, and business intelligence**, making it a strong portfolio project for Data Analyst roles.
