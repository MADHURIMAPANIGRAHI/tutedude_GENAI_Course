# Assignment 1 - Task 3: Product Pricing (Dictionaries)

price_dict = {
    "Laptop": 950.00,
    "Wireless Mouse": 25.50,
    "Mechanical Keyboard": 70.00,
    "Headphones": 120.00,
    "Webcam": 45.00,
    "Monitor": 180.00
}

print("Initial price dictionary:")
print(price_dict)

# 2. Small code blocks for dictionary operations

# Add a new product with price to price_dict
price_dict["USB Hub"] = 15.00
print("\nAfter adding 'USB Hub':")
print(price_dict)

# Update the price of an existing product
price_dict["Laptop"] = 920.00
print("\nAfter updating price of 'Laptop':")
print(price_dict)

# Remove a product by name (handling the case when the product does not exist)
product_to_remove = "Webcam"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"\nSuccessfully removed '{product_to_remove}'.")
else:
    print(f"\nProduct '{product_to_remove}' not found.")

# Trying to remove a product that does not exist
missing_product = "Smartwatch"
if missing_product in price_dict:
    del price_dict[missing_product]
    print(f"Successfully removed '{missing_product}'.")
else:
    print(f"Product '{missing_product}' does not exist, nothing to delete.")

print("\nUpdated price dictionary:")
print(price_dict)

# 3. Print the average price of all products (using dictionary operations and arithmetic)
total_price = sum(price_dict.values())
product_count = len(price_dict)
average_price = total_price / product_count

print("\nAverage price of all products:", round(average_price, 2))

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("\nExtra (Optional):")
print(f"Product with highest price: {max_product} (${price_dict[max_product]})")
print(f"Product with lowest price: {min_product} (${price_dict[min_product]})")
