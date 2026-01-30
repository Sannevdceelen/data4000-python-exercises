#Exercise 2: Credit Score Evaluator (Conditionals)
#Concepts: Input, int conversion, if/elif/else, logical operators, chained comparisons

score=int(input("What is your credit score? "))

if score < 300 or score > 850:
    print("Invalid score.")
else:
    if score >= 750:
        message = "Excellent - Loan Approved"
        approved = True
    elif 700 <= score < 750:
        message = "Good - Loan Approved with Review"
        approved = True
    elif 600 <= score < 700:
        message = "Fair - Loan Conditional"
        approved = True
    else:
        message = "Poor - Loan Denied"
        approved = False

    if approved:
        message = message + ". Interest rate: Low"
    else:
        message = message + ". Seek credit improvement."

    print(message)
