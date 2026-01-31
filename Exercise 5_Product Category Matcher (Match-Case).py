#Exercise 5: Product Category Matcher (Match-Case)
#Concepts: Match statements, string comparisons (lower, startswith), input stripping/lowercasing.
# 1) Ask for the product name
product_input = input("What's the product name? ")

# 2) Normalize spacing and casing
# split() removes extra spaces, join() puts single spaces back
product = " ".join(product_input.lower().split())

# 3) Get first word (useful for cases like "tech phone")
first_word = product.split()[0] if product != "" else ""

# 4) Categorize
if first_word.startswith("tech"):
    category = "High Margin"
else:
    match first_word:
        case "electronics" | "gadget":
            category = "High Margin"
        case "clothing" | "apparel":
            category = "Medium Margin"
        case "food" | "grocery":
            category = "Low Margin"
        case _:
            category = "Uncategorized - Review Needed"

# 5) Output
print(f"Product: {product} | Category: {category}")
