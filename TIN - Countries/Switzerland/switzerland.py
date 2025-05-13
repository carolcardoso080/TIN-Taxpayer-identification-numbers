from random import randint

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes dashes, dots, and spaces from a Swiss tin.
    """
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Swiss tin (CHE number) based on its check digit.
    """
    tin = remove_symbols(tin)
    if len(tin) != 9 or not tin.isdigit():
        return False
    base, check_digit = tin[:-1], int(tin[-1])
    return _calculate_digit(base) == check_digit

# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the check digit for a Swiss tin (CHE number).
    """
    weights = [5, 4, 3, 2, 7, 6, 5, 4]
    total = sum(int(d) * w for d, w in zip(base, weights))
    remainder = total % 11
    result = 11 - remainder
    if result == 10:
        return -1  # Invalid, never used
    elif result == 11:
        return 0
    return result

def format_tin(tin):  # type: (str) -> str
    """
    Formats a Swiss tin in the standard format (CHE-123.456.789).
    """
    tin = remove_symbols(tin)
    if len(tin) != 9:
        return None
    return f"CHE-{tin[:3]}.{tin[3:6]}.{tin[6:]}"

# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a valid Swiss tin (CHE number).
    """
    while True:
        base = str(randint(10000000, 99999999))
        dv = _calculate_digit(base)
        if dv >= 0:
            return base + str(dv)

# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your Swiss tin: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")