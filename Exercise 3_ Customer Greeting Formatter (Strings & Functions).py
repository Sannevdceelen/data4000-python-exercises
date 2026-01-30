#Exercise 3: Customer Greeting Formatter (Strings & Functions)
#Concepts: String methods (strip, title, split, lower), functions with parameters, defaults, return values.

def format_greeting(name: str, title: str = "Customer") -> str:
    """
    Return a greeting like: 'Hello, John (Customer)!'
    If name is empty or only spaces, return: 'Hello, Valued Customer!'.
    """

    # 1) Remove leading and trailing spaces
    cleaned_name = name.strip()

    # 2) Handle empty input
    if cleaned_name == "":
        return "Hello, Valued Customer!"

    # 3) Fix capitalization: 'john doe' -> 'John Doe'
    cleaned_name = cleaned_name.title()

    # 4) Split into words and take the first one as the first name
    parts = cleaned_name.split()
    first_name = parts[0]

    # 5) Build and return the final greeting string
    return f"Hello, {first_name} ({title})!"


# -------- main program --------

full_name = input("What's your full name? ")

# Call the function and store its result
greeting = format_greeting(full_name)

# Print the result
print(greeting)
