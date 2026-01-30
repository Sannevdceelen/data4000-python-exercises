#Exercise1: Profit Margin Calculator (Variables & Basic Arithmetic)
#concepts: input, float variables, arithmetic, f-string formatting, if/else

revenue = float(input("What is the revenue? "))
cost = float(input("What is the cost? "))
profit = revenue - cost
if revenue <= 0 :
    print("invalid revenue amount.")
else:
    margin = (profit / revenue) * 100
    print(f"profit: ${profit:,.2f} | Margin: {margin:,.2f}%")