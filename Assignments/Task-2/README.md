# Assignment 2: Python - Control Flow (Conditionals & Loops)

Student Name: Madhurima  
Course: TuteDude GenAI Course  
Topic: Python Control Flow (Conditionals, For/While Loops, Break & Continue)

---

## Overview

This assignment contains order processing and sales calculation utilities developed for an e-commerce store. The solutions focus strictly on control flow concepts:
- `if`, `elif`, and `else` conditional branching for tiered discounts.
- `for` loops for batch order processing and iteration.
- `while` loops for building interactive command-line menus.
- `break` and `continue` statements for loop interruption and skipping.

Per assignment instructions and restrictions, solutions do not use functions, classes, file operations, or external packages.

---

## File Structure

- `task1_discounts.py`: Takes an order amount from the user, validates that the input is a valid positive number, applies tiered discount rules (15%, 10%, 7%, 0%), and prints the final amount. Also includes the extra tax calculation.
- `task2_orders.py`: Uses a `for` loop to process a batch of order amounts `[1200, 2500, 800, 1750, 3000]`, displays a summary table (`order_amount -> discount% -> final_amount`), computes total revenue, and counts discounted orders.
- `task3_menu.py`: Implements an interactive `while True` loop menu allowing users to add orders (option 1), view all orders and totals (option 2), or quit (option q). Uses `continue` for input errors and `break` to exit.
- `task4_loop_control.py`: Iterates through daily sales figures `[200, 150, 0, 400, 50, -1, 300]`, using `break` on corrupted data (`-1`), `continue` on zero-sale days (`0`), and accumulating valid sales.
- `README.md`: Assignment documentation and execution guide.

---

## How to Run

Navigate into the `Task-2` folder and run each script with Python:

1. Task 1:
```bash
python task1_discounts.py
```

2. Task 2:
```bash
python task2_orders.py
```

3. Task 3:
```bash
python task3_menu.py
```

4. Task 4:
```bash
python task4_loop_control.py
```