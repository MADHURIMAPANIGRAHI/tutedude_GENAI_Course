# Assignment 1 - Task 2: Categories (Sets)

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Audio",
    "Accessories",
    "Display",
    "Accessories",
    "Accessories"
]

# 1. Create a set of categories called categories_set
categories_set = set(categories)
print("Initial categories set (duplicates removed):")
print(categories_set)

# Adding a new category
categories_set.add("Gaming")
print("\nAfter adding 'Gaming':")
print(categories_set)

# Trying to re-add an existing category
categories_set.add("Electronics")
print("\nAfter trying to add duplicate 'Electronics':")
print(categories_set)
print("(Duplicates are ignored by the set)")

# 3. Check whether a category exists in the set (print boolean result)
check_existing = "Audio" in categories_set
check_missing = "Clothing" in categories_set

print("\nMembership check:")
print("Is 'Audio' in categories_set?:", check_existing)
print("Is 'Clothing' in categories_set?:", check_missing)

# Extra (optional): Get total number of unique categories using a set
total_unique = len(categories_set)
print("\nExtra (Optional):")
print("Total number of unique categories:", total_unique)
