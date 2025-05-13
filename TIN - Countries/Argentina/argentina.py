from random import randint, choice

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
    Validates an Argentine tin based on its structure and check digit.
    """
    tin = remove_symbols(tin)
    if len(tin) != 11 or tin[0] not in "23" or tin[1] not in "03456789":
        return False
    base, check_digit = tin[:-1], int(tin[-1])
    return _calculate_digit(base) == check_digit

# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the check digit for a given tin base.
    """
    weights = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    total = sum(int(d) * w for d, w in zip(base, weights))
    remainder = total % 11
    if remainder == 10:
        return 9 if base.startswith(('20', '23', '24', '27')) else 0
    return remainder

def format_tin(tin):  # type: (str) -> str
    """
    Formats an Argentine tin for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) != 11:
        return None
    return "{}-{}-{}".format(tin[:2], tin[2:10], tin[10])

# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a random valid Argentine tin.
    """
    prefix = choice(['20', '23', '24', '27', '30', '33', '34'])
    base_number = str(randint(10000000, 99999999))  # Ensure 8-digit base
    base = prefix + base_number
    check_digit = _calculate_digit(base)
    return base + str(check_digit)

# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your tin: ")
print(is_valid(user_tin))
print(f"Formatted tin: {format_tin(user_tin)}")