# Assignment 1 - Task 1: Product Collections (Lists and Tuples)

# 1. Create a list named products
products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Headphones",
    "Webcam",
    "Monitor"
]

print("Initial products list:")
print(products)

# 2. Create a tuple named sample_product that stores (product_name, price, category)
sample_product = ("Laptop", 950.00, "Electronics")
print("\nSample product tuple:")
print(sample_product)

# 3. Print the 2nd and last product from the products list
# Index 1 is the second item, index -1 is the last item
second_product = products[1]
last_product = products[-1]

print("\nSecond product:", second_product)
print("Last product:", last_product)

# 4. Append two new product names to products and then print the updated list
products.append("USB Hub")
products.append("Desk Mat")

print("\nUpdated products list after appending:")
print(products)

# Since tuples cannot be modified directly, we convert to a list first
product_list = list(sample_product)
product_list[1] = 899.99  # change price
updated_sample_product = tuple(product_list)

print("\nExtra (Optional):")
print("Original tuple:", sample_product)
print("Updated tuple with new price:", updated_sample_product)
