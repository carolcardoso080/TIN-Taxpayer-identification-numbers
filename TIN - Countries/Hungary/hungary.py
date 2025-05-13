from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a string.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATE HUNGARIAN tin
def is_valid(tin):
    """Validates a Hungarian tin."""
    tin = remove_symbols(tin)
    if len(tin) != 10 or not tin.isdigit():
        return "Invalid Hungarian tin: Must contain exactly 10 numeric digits."
    expected_control_digit = calculate_control_digit(tin[:-1])
    return "Valid Hungarian tin." if tin[-1] == expected_control_digit else "Invalid Hungarian tin: Incorrect control digit."

# CONTROL DIGIT CALCULATION (MODULO 11)
def calculate_control_digit(number):
    """Calculates the control digit for Hungarian tin using Modulo 11."""
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Weights for the first 9 digits
    total = sum(int(number[i]) * weights[i] for i in range(9))
    control_digit = total % 11
    return str(control_digit)

# FORMAT HUNGARIAN tin FOR DISPLAY
def format_tin(tin):
    """Formats the Hungarian tin for display."""
    tin = remove_symbols(tin)
    if len(tin) != 10:
        return None
    return f"{tin[:3]} {tin[3:6]} {tin[6:9]} {tin[9]}"


# GENERATE VALID HUNGARIAN tin
def generate_tin():
    """Generates a valid Hungarian tin (Adóazonosító jel)."""
    first_digit = str(randint(1, 8))  # The first digit is between 1 and 8
    sequential_numbers = str(randint(10000000, 99999999))  # 8 random digits
    partial_tin = first_digit + sequential_numbers
    control_digit = calculate_control_digit(partial_tin)
    return f"{partial_tin}{control_digit}"


# EXAMPLES OF USAGE
def example_usage():
    generated_tin = generate_tin()
    print(f"Generated Hungarian tin: {generated_tin} - Valid? {is_valid(generated_tin)}")

    user_input = input("Enter your Hungarian tin: ")
    print(is_valid(user_input))
    print(f"Formatted tin: {format_tin(user_input)}")

# Run example
example_usage()
