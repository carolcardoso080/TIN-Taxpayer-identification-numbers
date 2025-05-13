from random import randint, choice

# REMOVE FORMATTING
def remove_symbols(dirty_tin):
    """Removes spaces, dots, and dashes from the Finnish tin."""
    return "".join(filter(lambda x: x.isalnum() or x in "+-A", dirty_tin))

# VALIDATE FINNISH tin
def is_valid(tin):
    """Validates a Finnish tin."""
    tin = remove_symbols(tin)
    if len(tin) != 11:
        return "Invalid Finnish tin: Must contain exactly 11 characters."

    # Extract components
    partial_tin = tin[:6] + tin[7:10]  # Remove century marker
    expected_control_char = calculate_control_character(partial_tin)
    
    if tin[-1] != expected_control_char:
        return "Invalid Finnish tin: Incorrect control character."
    
    return "Valid Finnish tin."


# CONTROL CHARACTER CALCULATION (Modulo 31 Algorithm)
def calculate_control_character(partial_tin):
    """Calculates the control character for a Finnish tin."""
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    number = int(partial_tin)
    return control_chars[number % 31]
    

# FORMAT FINNISH tin FOR DISPLAY
def format_tin(tin):
    """Formats the Finnish tin for display."""
    tin = remove_symbols(tin)
    return f"{tin[:6]}{tin[6]}{tin[7:]}"
    

# GENERATE VALID FINNISH tin
def generate():
    """Generates a valid Finnish tin (Henkilötunnus) with a correct control character."""
    day = randint(1, 28)  # Avoid February 30+
    month = randint(1, 12)
    year = randint(1800, 2099)
    
    # Define century marker
    if 1800 <= year <= 1899:
        century_marker = "+"
    elif 1900 <= year <= 1999:
        century_marker = "-"
    else:
        century_marker = "A"
    
    yy = str(year)[-2:]
    dd = f"{day:02}"
    mm = f"{month:02}"
    
    personal_identifier = f"{randint(0, 999):03}"  # 3-digit unique number
    gender_digit = randint(1, 9) * 2 - 1  # Odd for males, even for females
    
    partial_tin = f"{dd}{mm}{yy}{personal_identifier}{gender_digit}"
    control_char = calculate_control_character(partial_tin)
    
    return f"{dd}{mm}{yy}{century_marker}{personal_identifier}{gender_digit}{control_char}"


# EXAMPLES OF USAGE
def example_usage():
    generated_tin = generate()
    print(f"Generated Finnish tin: {generated_tin} - Valid? {is_valid(generated_tin)}")

    user_input = input("Enter your Finnish tin: ")
    print(is_valid(user_input))
    print(f"Formatted tin: {format_tin(user_input)}")

# Run example
example_usage()