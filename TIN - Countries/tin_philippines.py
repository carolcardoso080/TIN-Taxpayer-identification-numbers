from random import randint, choice

# REMOVE FORMATTING
def remove_symbols(dirty_tin):
    """Remove spaces, dots, and hyphens from the input string."""
    return "".join(filter(str.isalnum, dirty_tin))


# FORMAT PHILIPPINES TIN FOR DISPLAY
def format_tin(tin):
    """Formats the Philippines TIN for display."""
    tin = remove_symbols(tin)
    if len(tin) == 9:
        return f"{tin[:6]}-{tin[6:9]}"
    elif len(tin) == 12:
        return f"{tin[:6]}-{tin[6:9]}-{tin[9:12]}"
    return None
    

# VALIDATE PHILIPPINES TIN
def is_valid(tin):
    """Validates a Philippines TIN."""
    tin = remove_symbols(tin)
    if len(tin) not in [9, 12] or not tin.isdigit():
        return "Invalid Philippines TIN: Must contain either 9 or 12 numeric digits."
    return "Valid Philippines TIN."


# GENERATE VALID PHILIPPINES TIN (INDIVIDUAL OR BUSINESS)
def generate(is_business=False):
    """Generates a valid Philippines TIN."""
    registration_number = str(randint(100000, 999999))  # 6-digit registration number
    branch_code = str(randint(100, 999)) if is_business else "000"  # 3-digit branch code
    classification = str(randint(100, 999))  # 3-digit classification
    
    return f"{registration_number}{branch_code}{classification}"

# EXAMPLES OF USAGE
def example_usage():
    generated_tin = generate(is_business=True)
    print(f"Generated Philippines TIN: {generated_tin} - Valid? {is_valid(generated_tin)}")

    user_input = input("Enter your Philippines TIN: ")
    print(is_valid(user_input))
    print(f"Formatted TIN: {format_tin(user_input)}")

# Run example
example_usage()
