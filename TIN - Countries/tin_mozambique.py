from random import randint

# REMOVE FORMATTING
def remove_symbols(dirty_tin):
    """Remove spaces, dots, and hyphens from the input string."""
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATE tin
def is_valid(tin):
    """Validates a Mozambique tin number."""
    tin = remove_symbols(tin)

    if len(tin) != 9:
        return "Invalid tin: Must have exactly 9 numeric digits."
    
    if not tin.isdigit():
        return "Invalid tin: Should contain only numbers."

    tin_base, given_check_digit = tin[:8], tin[8]
    calculated_check_digit = calculate_check_digit(tin_base)

    if calculated_check_digit != str(given_check_digit):  # Convertendo para string para comparação correta
        return "Invalid tin: Check digit does not match."

    return "Valid tin"

# CALCULATE CHECK DIGIT
def calculate_check_digit(dirty_tin):
    """Calculate the check digit for an 8-digit tin."""
    if len(dirty_tin) != 8 or not dirty_tin.isdigit():
        return None
    
    weights = [2, 3, 4, 5, 6, 7, 8, 9]  # Pesos fixos para cada dígito
    total = sum(int(dirty_tin[i]) * weights[i] for i in range(8))
    
    check_digit = (10 - (total % 10)) % 10
    return str(check_digit)

# GENERATE VALID tin
def generate():
    """Generates a valid 9-digit tin for Mozambique."""
    tin_base = "".join(str(randint(0, 9)) for _ in range(8))
    check_digit = calculate_check_digit(tin_base)
    return tin_base + check_digit

# FORMAT tin
def format_tin(tin):
    """Formats a Mozambique tin for display."""
    tin = remove_symbols(tin)

    if len(tin) != 9:
        return None
    return f"{tin[:3]}.{tin[3:6]}.{tin[6:]}"

# EXAMPLES
def example_usage():
    # Generate a valid tin
    generated_tin = generate()
    print(f"Generated tin: {generated_tin} - Valid? {is_valid(generated_tin)}")

    # User input validation
    user_input = input("Enter your Mozambique tin: ")
    print(is_valid(user_input))

    formatted_input = format_tin(user_input)
    if formatted_input:
        print(f"Formatted tin: {formatted_input}")

# Run example
example_usage()