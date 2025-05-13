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
    Validates a Colombian tin based on its structure and check digit.
    """
    tin = remove_symbols(tin)
    if len(tin) < 9 or len(tin) > 10:
        return False
    base, check_digit = tin[:-1], int(tin[-1])
    return _calculate_digit(base) == check_digit

# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the check digit for a given tin base.
    """
    weights = [71, 67, 59, 53, 47, 43, 41, 37, 29, 23]
    total = sum(int(d) * w for d, w in zip(base[::-1], weights[-len(base):]))
    remainder = total % 11
    if remainder in [0, 1]:
        return 0
    return 11 - remainder

def format_tin(tin):  # type: (str) -> str
    """
    Formats a Colombian tin for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) < 9 or len(tin) > 10:
        return None
    return "{}.{}.{}/{}".format(tin[:-6], tin[-6:-3], tin[-3:-1], tin[-1])

# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a random valid Colombian tin.
    """
    base_number = str(randint(100000000, 999999999))
    check_digit = _calculate_digit(base_number)
    return base_number + str(check_digit)

# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your tin: ")
print(is_valid(user_tin))
print(f"Formatted tin: {format_tin(user_tin)}")