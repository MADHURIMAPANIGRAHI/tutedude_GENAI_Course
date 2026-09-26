# Assignment 2 - Task 2: Process Multiple Orders (for loop)

# 1. Given list of order amounts
orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0.0
discount_count = 0

print("Orders Summary Table:")
print("Order Amount -> Discount% -> Final Amount")
print("-----------------------------------------")

# Process each order using a for loop
for order_amount in orders:
    # Apply discount rules from Task 1
    if order_amount >= 2000:
        discount_percent = 15
    elif order_amount >= 1500:
        discount_percent = 10
    elif order_amount >= 1000:
        discount_percent = 7
    else:
        discount_percent = 0

    discount_amount = (order_amount * discount_percent) / 100
    final_amount = order_amount - discount_amount

    # Add to total revenue
    total_revenue = total_revenue + final_amount

    # Count orders that received a discount
    if discount_percent > 0:
        discount_count = discount_count + 1

    print(f"{order_amount} -> {discount_percent}% -> {round(final_amount, 2)}")

print("-----------------------------------------")
print("Total revenue after discounts:", round(total_revenue, 2))

print("Number of orders that received a discount:", discount_count)
