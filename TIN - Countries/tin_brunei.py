from random import randint, choice

# REMOVE FORMATTING
def remove_symbols(dirty_tin):
    """Remove spaces, dots, and hyphens from the input string."""
    return "".join(filter(str.isalnum, dirty_tin))

# VALIDATE TIN
def is_valid(tin):
    """Validates a Brunei TIN."""
    tin = remove_symbols(tin)

    if len(tin) != 10:
        return "Invalid TIN: Must have exactly 10 alphanumeric characters."

    if not tin[:2].isalpha() or not tin[2:].isdigit():
        return "Invalid TIN: Must start with letters (BN or BP) and end with 8 digits."

    return "Valid TIN"

# GENERATE VALID TIN
def generate():
    """Generates a valid 10-character Brunei TIN."""
    prefix = choice(["BN", "BP"])  # BN for individuals, BP for companies
    numeric_part = "".join(str(randint(0, 9)) for _ in range(8))
    return prefix + numeric_part


# FORMAT TIN
def format_tin(tin):
    """Formats a Brunei TIN for display."""
    tin = remove_symbols(tin)

    if len(tin) != 10:
        return None
    return f"{tin[:2]}-{tin[2:6]}-{tin[6:]}"

# EXAMPLES
def example_usage():
    # Generate a valid TIN
    generated_tin = generate()
    print(f"Generated TIN: {generated_tin} - Valid? {is_valid(generated_tin)}")

    # User input validation
    user_input = input("Enter your Brunei TIN: ")
    print(is_valid(user_input))

    formatted_input = format_tin(user_input)
    if formatted_input:
        print(f"Formatted TIN: {formatted_input}")

# Run example
example_usage()
