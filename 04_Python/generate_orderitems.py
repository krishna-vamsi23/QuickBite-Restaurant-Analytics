import pandas as pd
import random

# ----------------------------
# Read Orders and Products
# ----------------------------

orders = pd.read_csv("02_Dataset/QuickBite_Orders.csv")
products = pd.read_excel("02_Dataset/QuickBite_Products.xlsx")

order_items = []

order_item_id = 1

# ----------------------------
# Generate Order Items
# ----------------------------

for _, order in orders.iterrows():

    # Each order contains 1 to 5 products
    number_of_products = random.randint(1,5)

    # Select random products
    selected_products = products.sample(number_of_products)

    for _, product in selected_products.iterrows():

        order_item = {

            "OrderItemID": f"OI{order_item_id:06}",

            "OrderID": order["OrderID"],

            "ProductID": product["ProductID"],

            "Quantity": random.randint(1,3),

            "UnitPrice": product["SellingPrice (€)"]

        }

        order_items.append(order_item)

        order_item_id += 1

# ----------------------------
# Convert to DataFrame
# ----------------------------

df = pd.DataFrame(order_items)

print(df.head())

# ----------------------------
# Save CSV
# ----------------------------

df.to_csv(
    "02_Dataset/QuickBite_OrderItems.csv",
    index=False
)

print("\nOrderItems dataset created successfully!")
print(f"Total Order Items: {len(df)}")