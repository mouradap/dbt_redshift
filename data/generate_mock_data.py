import random
import csv
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Constants
NUM_CUSTOMERS = 100
NUM_PRODUCTS = 50
NUM_ORDERS = 500

# File paths
CUSTOMERS_FILE = "customers.csv"
PRODUCTS_FILE = "products.csv"
ORDERS_FILE = "orders.csv"

# Generate mock data
def generate_customers():
    customers = []
    for customer_id in range(1, NUM_CUSTOMERS + 1):
        customers.append({
            "customer_id": customer_id,
            "customer_name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "signup_date": fake.date_between(start_date="-5y", end_date="today").isoformat(),
        })
    return customers

def generate_products():
    products = []
    for product_id in range(1, NUM_PRODUCTS + 1):
        products.append({
            "product_id": product_id,
            "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),
            "category": random.choice(["Electronics", "Clothing", "Books", "Toys", "Home"]),
            "price": round(random.uniform(5.0, 500.0), 2),
        })
    return products

def generate_orders(customers, products):
    orders = []
    for order_id in range(1, NUM_ORDERS + 1):
        customer = random.choice(customers)
        product = random.choice(products)
        order_date = fake.date_between(start_date="-3y", end_date="today")
        orders.append({
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "product_id": product["product_id"],
            "order_date": order_date.isoformat(),
            "quantity": random.randint(1, 5),
            "total_amount": round(product["price"] * random.randint(1, 5), 2),
        })
    return orders

# Write CSV files
def write_csv(filename, data, fieldnames):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Main function
def main():
    print("Generating mock data...")

    # Generate data
    customers = generate_customers()
    products = generate_products()
    orders = generate_orders(customers, products)

    # Write to CSV files
    write_csv(CUSTOMERS_FILE, customers, ["customer_id", "customer_name", "email", "phone", "address", "signup_date"])
    write_csv(PRODUCTS_FILE, products, ["product_id", "product_name", "category", "price"])
    write_csv(ORDERS_FILE, orders, ["order_id", "customer_id", "product_id", "order_date", "quantity", "total_amount"])

    print(f"Mock data generated successfully:")
    print(f"  - {CUSTOMERS_FILE}")
    print(f"  - {PRODUCTS_FILE}")
    print(f"  - {ORDERS_FILE}")

if __name__ == "__main__":
    main()
