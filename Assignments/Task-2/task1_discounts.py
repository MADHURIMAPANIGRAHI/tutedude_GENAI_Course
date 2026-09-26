# Assignment 2 - Task 1: Discount Rules (if / elif / else)

# 1. Read integer order amount from user
user_input = input("Enter order amount: ").strip()

# 2. Check if the input is a valid numeric integer
if not user_input.isdigit():
    print("Error: Invalid input. Please enter a valid positive number.")
    exit()

order_amount = int(user_input)

# 3. Apply discount rules using if / elif / else
if order_amount >= 2000:
    discount_percent = 15
elif order_amount >= 1500:
    discount_percent = 10
elif order_amount >= 1000:
    discount_percent = 7
else:
    discount_percent = 0

# Calculate discount value and final amount
discount_amount = (order_amount * discount_percent) / 100
final_amount = order_amount - discount_amount

print("\nOrder Summary:")
print("Original Amount:", order_amount)
print("Discount:", str(discount_percent) + "%")
print("Discount Amount:", round(discount_amount, 2))
print("Final Amount:", round(final_amount, 2))

subtotal = final_amount
tax = (subtotal * 5) / 100
total_with_tax = subtotal + tax

print("\nExtra (Tax Breakdown):")
print("Subtotal:", round(subtotal, 2))
print("Tax (5%):", round(tax, 2))
print("Total with Tax:", round(total_with_tax, 2))
