from random import randint, choice

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes any non-digit characters from a Cuban tin.
    """
    return "".join(filter(str.isdigit, dirty_tin))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Cuban tin for companies (9-digit version).
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
    Calculates the check digit for a Cuban tin (company).
    """
    weights = [3, 2, 7, 6, 5, 4, 3, 2]
    total = sum(int(d) * w for d, w in zip(base, weights))
    remainder = total % 11
    if remainder == 0:
        return 0
    elif remainder == 1:
        return 1
    return 11 - remainder


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Cuban tin in a readable way (XXX-XXX-XXX).
    """
    tin = remove_symbols(tin)
    if len(tin) != 9:
        return None
    return f"{tin[:3]}-{tin[3:6]}-{tin[6:]}"


# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a valid 9-digit Cuban tin (for companies).
    """
    base = str(randint(10000000, 99999999))
    dv = _calculate_digit(base)
    return base + str(dv)


# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your Cuban tin: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")