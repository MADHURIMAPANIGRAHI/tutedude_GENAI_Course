# Assignment 1 - Task 4: Combined Operations

products = [
    "Laptop",
    "Wireless Mouse",
    "Mechanical Keyboard",
    "Headphones",
    "Webcam",
    "Monitor",
    "USB Hub",
    "Desk Mat"
]

# Prices for the products
price_dict = {
    "Laptop": 920.00,
    "Wireless Mouse": 25.50,
    "Mechanical Keyboard": 70.00,
    "Headphones": 120.00,
    "Webcam": 45.00,
    "Monitor": 180.00,
    "USB Hub": 15.00,
    "Desk Mat": 12.00
}

# Categories for the products
product_categories = {
    "Laptop": "Electronics",
    "Wireless Mouse": "Accessories",
    "Mechanical Keyboard": "Accessories",
    "Headphones": "Audio",
    "Webcam": "Accessories",
    "Monitor": "Display",
    "USB Hub": "Accessories",
    "Desk Mat": "Accessories"
}

# 1. Create a list of tuples named catalog: (product_name, price, category)
catalog = []
for item in products:
    price = price_dict[item]
    category = product_categories[item]
    catalog.append((item, price, category))

print("Product Catalog (List of Tuples):")
for record in catalog:
    print(record)

# 2. From catalog, create a new dictionary category_to_products
# Maps each category to a list of product names in that category
category_to_products = {}
for name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(name)

print("\nCategory to Products Mapping:")
for cat, prods in category_to_products.items():
    print(f"{cat}: {prods}")

# 3. Print all products that belong to the category with the maximum number of products
max_category = None
max_count = 0

for cat, prods in category_to_products.items():
    if len(prods) > max_count:
        max_count = len(prods)
        max_category = cat

print(f"\nCategory with the most products: '{max_category}' ({max_count} items)")
print("Products in this category:")
for p in category_to_products[max_category]:
    print("-", p)
