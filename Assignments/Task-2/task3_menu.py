# Assignment 2 - Task 3: User Menu (while loop + break/continue)

# List to keep track of added order amounts
order_list = []

while True:
    print("\nMenu Options:")
    print("1 - Add order amount")
    print("2 - Show all orders and totals")
    print("q - Quit")

    choice = input("Enter choice: ").strip()

    # Quit menu using break
    if choice == "q" or choice == "Q":
        print("Exiting program. Thank you!")
        break

    # Add order amount
    if choice == "1":
        amount_input = input("Enter order amount: ").strip()

        # Check if input is digits
        if not amount_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        order_val = int(amount_input)
        order_list.append(order_val)
        print(f"Order of {order_val} added successfully.")
        continue

    # Show all orders and calculated totals
    if choice == "2":
        if len(order_list) == 0:
            print("No orders added yet.")
            continue

        print("\nOrders Breakdown:")
        total_original = 0.0
        total_discounted = 0.0

        for order in order_list:
            if order >= 2000:
                disc_pct = 15
            elif order >= 1500:
                disc_pct = 10
            elif order >= 1000:
                disc_pct = 7
            else:
                disc_pct = 0

            disc_amount = (order * disc_pct) / 100
            final_order = order - disc_amount

            total_original = total_original + order
            total_discounted = total_discounted + final_order

            print(f"- Amount: {order}, Discount: {disc_pct}%, Final: {round(final_order, 2)}")

        print("-------------------------------")
        print("Total Original Amount:", round(total_original, 2))
        print("Total After Discounts:", round(total_discounted, 2))
        continue

    # Handle invalid menu option and re-show menu
    print("Invalid option. Please enter 1, 2, or q.")
    continue
