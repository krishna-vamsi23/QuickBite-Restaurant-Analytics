import pandas as pd
from faker import Faker
import random

# -------------------------------
# Create Faker Object
# -------------------------------
faker = Faker("de_DE")

# Empty list
orders = []

# -------------------------------
# Generate 100,000 Orders
# -------------------------------

for i in range(100000):

    order = {

        "OrderID": f"O{i+1:06}",

        "CustomerID": f"C{random.randint(1,5000):05}",

        "EmployeeID": f"E{random.randint(1,150):03}",

        "StoreID": f"S{random.randint(1,10):03}",

        "OrderDate": faker.date_between(
            start_date="-2y",
            end_date="today"
        ),

        "OrderTime": faker.time(),

        "OrderType": random.choices(
            ["Dine-In", "Takeaway", "Delivery"],
            weights=[45, 35, 20]
        )[0],

        "TotalAmount": round(
            random.uniform(5, 45),
            2
        )

    }

    orders.append(order)

# -------------------------------
# Convert to DataFrame
# -------------------------------

df = pd.DataFrame(orders)

print(df.head(10))

# -------------------------------
# Save as CSV
# -------------------------------

df.to_csv(
    "02_Dataset/QuickBite_Orders.csv",
    index=False
)

print("\nOrders dataset created successfully!")
print(f"Total Orders Generated: {len(df)}")