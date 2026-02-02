# Bonus Challenge: Integrated Decision Tool
# Combines functions, conditionals, and match-case statements

def is_profitable(revenue: float, cost: float) -> bool:
    """
    Returns True if revenue is greater than cost,
    otherwise returns False.
    """
    return revenue > cost


def main():
    # Prompt for inputs
    revenue = float(input("Enter business revenue: "))
    cost = float(input("Enter business cost: "))
    category_input = input("Enter product category: ")

    # Normalize category input
    category = category_input.strip().lower()

    # Check profitability
    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profit: ${profit:,.2f}")

        # Suggest investment decision based on category
        match category:
            case "high margin":
                decision = "Reinvest"
            case "medium margin":
                decision = "Maintain current strategy"
            case "low margin":
                decision = "Review costs and proceed cautiously"
            case _:
                decision = "Further analysis required"

        print(f"Suggested decision: {decision}")
    else:
        print("The business is not profitable.")
        print("Suggested decision: Do not invest at this time.")


# Run the main function
main()
