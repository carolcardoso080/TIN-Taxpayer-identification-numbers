from random import randint, choice


# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a string.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATION FUNCTION
def is_valid(tin):  # type: (str) -> str
    """
    Validates an Israeli tin, including the checksum digit.

    Args:
        tin (str): tin to validate.

    Returns:
        str: 'Valid tin' if valid, otherwise 'Invalid tin'.
    """
    tin = remove_symbols(tin)

    if len(tin) != 9 or not tin.isdigit():
        return "Invalid tin: Must be exactly 9 numeric digits."

    # Checksum validation
    total = 0
    for i, digit in enumerate(tin):
        num = int(digit) * (1 + (i % 2))  # Alternates between multiplying by 1 and 2
        total += num if num < 10 else num - 9  # Subtract 9 if num >= 10
    return "Valid tin" if total % 10 == 0 else "Invalid tin: Checksum failed."

# GENERATE FUNCTION
def generate_tin():  # type: () -> str
    """
    Generates a valid random Israeli tin.

    Returns:
        str: A valid randomly generated tin.
    """
    base_number = f"{randint(10000000, 99999999)}"  # Generate the first 8 digits
    total = 0
    for i, digit in enumerate(base_number):
        num = int(digit) * (1 + (i % 2))  # Alternates between multiplying by 1 and 2
        total += num if num < 10 else num - 9  # Subtract 9 if num >= 10
    check_digit = (10 - (total % 10)) % 10  # Calculate the checksum digit
    return base_number + str(check_digit)

# FORMAT FUNCTION
def format_tin(tin):  # type: (str) -> str
    """
    Formats an Israeli tin with appropriate dashes for display.

    Args:
        tin (str): tin to format.

    Returns:
        str: Formatted tin or None if invalid.
    """
    tin = remove_symbols(tin)

    if is_valid(tin) == "Valid tin":
        return f"{tin[:3]}-{tin[3:9]}"
    return None

# USER INPUT VALIDATION
def is_valid_user_input(user_input):  # type: (str) -> str
    """
    Validates user input as a valid Israeli tin.

    Args:
        user_input (str): User input to validate.

    Returns:
        str: The validity of the tin.
    """
    user_input = remove_symbols(user_input)

    if is_valid(user_input) == "Valid tin":
        return f"Valid tin: {user_input}"
    return "Invalid tin format."

# USAGE EXAMPLES
def example_usage():
    # Generate examples
    generated_id = generate_tin()
    print(f"Generated ID: {generated_id} - Valid? {is_valid(generated_id)}")
    print(f"Formatted ID: {format_tin(generated_id)}")

    # User input
    user_input = input("Enter an Israeli tin (with or without symbols): ")
    print(is_valid_user_input(user_input))
    print(f"Formatted ID: {format_tin(user_input)}")

# Run the example usage
example_usage()
