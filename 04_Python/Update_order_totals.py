import pandas as pd

# -----------------------------
# Read Orders and OrderItems
# -----------------------------

orders = pd.read_csv("02_Dataset/QuickBite_Orders.csv")

order_items = pd.read_csv("02_Dataset/QuickBite_OrderItems.csv")

# -----------------------------
# Calculate Line Total
# -----------------------------

order_items["LineTotal"] = (
    order_items["Quantity"] *
    order_items["UnitPrice"]
)

# -----------------------------
# Calculate Order Total
# -----------------------------

totals = (
    order_items
    .groupby("OrderID")["LineTotal"]
    .sum()
    .reset_index()
)

totals.rename(
    columns={
        "LineTotal": "TotalAmount"
    },
    inplace=True
)

# -----------------------------
# Merge with Orders
# -----------------------------

orders = orders.drop(columns=["TotalAmount"])

orders = orders.merge(
    totals,
    on="OrderID",
    how="left"
)

orders["TotalAmount"] = (
    orders["TotalAmount"]
    .round(2)
)

# -----------------------------
# Save
# -----------------------------

orders.to_csv(
    "02_Dataset/QuickBite_Orders.csv",
    index=False
)

print("Orders updated successfully!")
print(orders.head())