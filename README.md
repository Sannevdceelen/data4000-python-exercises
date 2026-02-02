# DATA 4000 – Python with AI Exercises

This repository contains solutions for the DATA 4000: Python with AI exercises.
The programs demonstrate core Python concepts including variables, conditionals,
functions, string methods, and match-case statements.

All code is written in Python 3 and intended to be run from the command line using VS Code.

---

## Exercise 1: Profit Margin Calculator
File: exercise1_profit_calculator.py

Prompts the user for revenue and cost values, calculates profit and profit margin,
and prints formatted output. If revenue is zero or negative, the program prints an
error message.

Assumptions:
- Revenue and cost are numeric inputs.
- Revenue must be greater than zero.

---

## Exercise 2: Credit Score Evaluator
File: exercise2_credit_score_evaluator.py

Evaluates a user’s credit score and determines loan eligibility based on predefined
score ranges. Outputs an approval decision and a follow-up message.

Assumptions:
- Credit scores are integers between 300 and 850.
- Scores outside this range are invalid.

---

## Exercise 3: Customer Greeting Formatter
File: exercise3_customer_greeting_formatter.py

Defines a function that formats a personalized greeting using the user’s name.
The input is cleaned, the first name is extracted, and a default title is applied
when no custom title is provided.

Assumptions:
- User input may include extra spaces or inconsistent capitalization.
- Empty input results in a generic greeting.

---

## Exercise 4: Tax Bracket Determiner
File: exercise4_tax_bracket_determiner.py

Determines a user’s tax bracket based on annual income and calculates an estimated
tax amount using conditional logic.

Assumptions:
- Income is provided as a numeric value.
- Negative income values are invalid.

---

## Exercise 5: Product Category Matcher
File: exercise5_product_category_matcher.py

Categorizes a product based on its name using string normalization and match-case
statements. Outputs the product name and its margin category.

Assumptions:
- Product names are normalized to lowercase and cleaned of extra spaces.
- Products not listed in predefined categories are marked for review.
