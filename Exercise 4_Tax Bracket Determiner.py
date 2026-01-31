#Exercise 4: Tax Bracket Determiner (Conditionals & Functions Returning Bool/Values)
#Concepts: Functions returning values (including bools), modulo (optional), if/elif/else, ternary expressions.

def get_tax_bracket(income: float) -> str:
    """
    Return the tax bracket as a string based on the income.
    - income < 0           -> "Invalid income."
    - income < 50,000      -> "Low (10%)"
    - 50,000 <= income < 100,000 -> "Medium (20%)"
    - income >= 100,000    -> "High (30%)"
    """

    if income < 0:
        return "Invalid income."
    elif income < 50000:
        bracket = "Low (10%)"
    elif income < 100000:
        bracket = "Medium (20%)"
    else:
        bracket = "High (30%)"

    # Bonus: simple ternary check
    # If income is even when rounded, mark it as "Deduction Eligible"
    deduction_note = " (Deduction Eligible)" if int(round(income)) % 2 == 0 else ""

    return bracket + deduction_note


# -------- main program --------

income_text = input("What's your annual income? ")
income = float(income_text)

bracket = get_tax_bracket(income)

if bracket == "Invalid income.":
    # Just show the error message
    print(bracket)
else:
    # Decide tax rate from the bracket text
    if "10%" in bracket:
        rate = 0.10
    elif "20%" in bracket:
        rate = 0.20
    else:
        rate = 0.30

    estimated_tax = income * rate

    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax:,.2f}")
