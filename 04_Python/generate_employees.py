import pandas as pd
from faker import Faker
import random

# Create Faker object for German names
faker = Faker("de_DE")

# Empty list to store employees
employees = []

# Generate 150 employees
for i in range(150):

    # Random Position
    position = random.choice([
        "Crew Member",
        "Shift Manager",
        "Assistant Manager",
        "Store Manager"
    ])

    # Hourly rate based on position
    if position == "Crew Member":
        hourly_rate = round(random.uniform(15, 17), 2)

    elif position == "Shift Manager":
        hourly_rate = round(random.uniform(18, 22), 2)

    elif position == "Assistant Manager":
        hourly_rate = round(random.uniform(23, 27), 2)

    else:
        hourly_rate = round(random.uniform(28, 35), 2)

    # Create one employee
    employee = {

        "EmployeeID": f"E{i+1:03}",

        "FirstName": faker.first_name(),

        "LastName": faker.last_name(),

        "Gender": random.choice([
            "Male",
            "Female"
        ]),

        "DateOfBirth": faker.date_of_birth(
            minimum_age=18,
            maximum_age=60
        ),

        "HireDate": faker.date_between(
            start_date="-5y",
            end_date="today"
        ),

        "Position": position,

        "Shift": random.choice([
            "Morning",
            "Afternoon",
            "Night"
        ]),

        "StoreID": random.choice([
            "S001",
            "S002",
            "S003",
            "S004",
            "S005",
            "S006",
            "S007",
            "S008",
            "S009",
            "S010"
        ]),

        "HourlyRate": hourly_rate,

        "EmploymentType": random.choice([
            "Full-Time",
            "Part-Time"
        ]),

        "EmploymentStatus": random.choice([
            "Active",
            "On Leave"
        ])

    }

    # Add employee to list
    employees.append(employee)

# Convert list into DataFrame
df = pd.DataFrame(employees)

# Display first 10 employees
print(df.head(10))

# Save to Excel
df.to_excel(
    "02_Dataset/QuickBite_Employees.xlsx",
    index=False
)

print("\nEmployee file created successfully!")
print(f"Total Employees Generated: {len(df)}")