from random import randint

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes all non-digit characters from the tin.
    """
    return "".join(filter(str.isdigit, dirty_tin))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Guinea-Bissau tin (tax ID).
    Must be 9 digits long and pass check digit verification.
    """
    tin = remove_symbols(tin)
    if len(tin) != 9 or not tin.isdigit():
        return False
    base, check_digit = tin[:8], int(tin[8])
    return _calculate_digit(base) == check_digit


# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the check digit for a Guinea-Bissau tin base.
    """
    weights = list(range(2, 10))  # [2, 3, 4, 5, 6, 7, 8, 9]
    total = sum(int(d) * w for d, w in zip(reversed(base), weights))
    remainder = total % 11
    digit = 11 - remainder
    return 0 if digit >= 10 else digit


# FORMATTING
#############

def format_tin(tin):  # type: (str) -> str
    """
    Formats a Guinea-Bissau tin into a readable form: XXX XXX XXX
    """
    tin = remove_symbols(tin)
    if len(tin) != 9:
        return None
    return f"{tin[:3]} {tin[3:6]} {tin[6:]}"


# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a random valid Guinea-Bissau tin.
    """
    base = str(randint(10000000, 99999999))
    check_digit = _calculate_digit(base)
    return base + str(check_digit)


# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your Guinea-Bissau tin: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")
