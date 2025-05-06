from random import randint, choice

# REMOVE FORMATTING
def remove_symbols(dirty_tin):
    """Remove spaces, dots, and hyphens from the input string."""
    return "".join(filter(str.isalnum, dirty_tin))
    

# VALIDATE CONGO TIN
def is_valid(tin):
    """Validates a Republic of Congo TIN."""
    tin = remove_symbols(tin)
    if len(tin) != 9 or not tin.isdigit():
        return "Invalid Republic of Congo TIN: Must contain exactly 9 numeric digits."
    
    base_number = list(map(int, tin[:-1]))  # Extract first 8 digits
    expected_control_digit = calculate_control_digit(base_number)
    actual_control_digit = int(tin[-1])
    
    if expected_control_digit != actual_control_digit:
        return "Invalid Republic of Congo TIN: Incorrect control digit."
    
    return "Valid Republic of Congo TIN."

# CONTROL DIGIT CALCULATION (Modulus Algorithm)
def calculate_control_digit(base_number):
    """Calculates the control digit for a Republic of Congo TIN."""
    weights = [2, 3, 4, 5, 6, 7, 2, 3]  # Weighting factors
    weighted_sum = sum(base_number[i] * weights[i] for i in range(8))
    control_digit = (10 - (weighted_sum % 10)) % 10  # Modulo 10 check
    return control_digit


# FORMAT CONGO TIN FOR DISPLAY
def format_tin(tin):
    """Formats the Republic of Congo TIN for display."""
    tin = remove_symbols(tin)
    return f"{tin[:3]} {tin[3:6]} {tin[6:9]}"

# GENERATE VALID CONGO TIN
def generate():
    """Generates a valid Republic of Congo TIN with a correct control digit."""
    base_number = [randint(0, 9) for _ in range(8)]  # First 8 digits
    control_digit = calculate_control_digit(base_number)  # Compute control digit
    tin = "".join(map(str, base_number)) + str(control_digit)
    return tin

# EXAMPLES OF USAGE
def example_usage():
    generated_tin = generate()
    print(f"Generated Congo TIN: {generated_tin} - Valid? {is_valid(generated_tin)}")

    user_input = input("Enter your Congo TIN: ")
    print(is_valid(user_input))
    print(f"Formatted TIN: {format_tin(user_input)}")

# Run example
example_usage()

