from random import randint

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dashes, and other symbols from a tin.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Bolivian tin based on its structure and check digit.
    """
    tin = remove_symbols(tin)
    if len(tin) < 7 or len(tin) > 10:
        return False
    base, check_digit = tin[:-1], int(tin[-1])
    return _calculate_digit(base) == check_digit

# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the check digit for a given tin base using modulo 11.
    """
    weights = [2, 3, 4, 5, 6, 7]
    total = 0
    for i, digit in enumerate(reversed(base)):
        total += int(digit) * weights[i % len(weights)]
    remainder = total % 11
    check_digit = 11 - remainder if remainder != 10 else 0
    return check_digit

def format_tin(tin):  # type: (str) -> str
    """
    Formats a Bolivian tin for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) < 7 or len(tin) > 10:
        return None
    return "{}.{}-{}".format(tin[:-5], tin[-5:-1], tin[-1])

# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a random valid Bolivian tin.
    """
    base_number = str(randint(1000000, 99999999))[:7]  # Ensure 7 to 8-digit base
    check_digit = _calculate_digit(base_number)
    return base_number + str(check_digit)

# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your tin: ")
print(is_valid(user_tin))
print(f"Formatted tin: {format_tin(user_tin)}")