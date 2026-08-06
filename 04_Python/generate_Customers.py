import pandas as pd
from faker import Faker
import random

# -----------------------------------
# Create Faker object
# -----------------------------------
faker = Faker("de_DE")

# Empty list to store customers
customers = []

# German cities
cities = [
    "Berlin",
    "Munich",
    "Hamburg",
    "Frankfurt",
    "Cologne",
    "Stuttgart",
    "Düsseldorf",
    "Leipzig",
    "Dresden",
    "Jena"
]

# -----------------------------------
# Generate 5000 customers
# -----------------------------------
for i in range(5000):

    # Random gender
    gender = random.choice(["Male", "Female"])

    # Generate gender-based first name
    if gender == "Male":
        first_name = faker.first_name_male()
    else:
        first_name = faker.first_name_female()

    last_name = faker.last_name()

    customer = {

        "CustomerID": f"C{i+1:05}",

        "FirstName": first_name,

        "LastName": last_name,

        "Gender": gender,

        "DateOfBirth": faker.date_of_birth(
            minimum_age=18,
            maximum_age=80
        ),

        "City": random.choice(cities),

        "RegistrationDate": faker.date_between(
            start_date="-5y",
            end_date="today"
        ),

        # 40% Loyalty Members
        "LoyaltyMember": random.choices(
            ["Yes", "No"],
            weights=[40, 60]
        )[0],

        "Email": faker.email()

    }

    customers.append(customer)

# -----------------------------------
# Convert to DataFrame
# -----------------------------------
df = pd.DataFrame(customers)

# Display first 10 records
print(df.head(10))

# -----------------------------------
# Export to Excel
# -----------------------------------
df.to_excel(
    "02_Dataset/QuickBite_Customers.xlsx",
    index=False
)

print("\nCustomer dataset created successfully!")
print(f"Total Customers Generated: {len(df)}")