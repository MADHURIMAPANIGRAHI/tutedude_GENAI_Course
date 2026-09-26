# Assignment 2 - Task 4: Loop Control with Conditions (break & continue)

# 1. Given list of daily sales figures
daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

print("Processing daily sales list:")

# Iterate through the list using a for loop
for sale in daily:
    # If value is -1, treat as corrupted data and break the loop
    if sale == -1:
        print(f"Corrupted data encountered ({sale}). Stopping processing.")
        break

    # If value is 0, treat as day with no sales and skip using continue
    if sale == 0:
        print("Day with 0 sales (skipping).")
        continue

    # For valid positive sales, add to total_sales and print running total
    total_sales = total_sales + sale
    print(f"Added sale: {sale} -> Running total: {total_sales}")

# 2. Print final total after loop ends
print("\nFinal total sales processed:", total_sales)
