from random import randint

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dashes, and other symbols from a TIN.
    """
    return "".join(filter(str.isalnum, dirty_tin))

# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Chinese TIN based on its structure and check digit.
    """
    tin = remove_symbols(tin)
    if len(tin) == 18:
        base, check_digit = tin[:-1], tin[-1]
        return _calculate_digit(base) == check_digit
    elif len(tin) == 15:
        return tin.isdigit()  # Old 15-digit TINs are numeric with no check digit
    return False

# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> str
    """
    Calculates the check digit for a given 18-digit TIN base.
    """
    weights = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
    charset = "0123456789ABCDEFGHJKLMNPQRTUWXY"
    total = sum(charset.index(d) * w for d, w in zip(base, weights))
    check_digit = (31 - (total % 31)) % 31
    return charset[check_digit]

def format_tin(tin):  # type: (str) -> str
    """
    Formats a Chinese TIN for readability and identifies if it's old or new.
    """
    tin = remove_symbols(tin)
    if len(tin) == 18:
        return "{} {} {} {} (New Regime)".format(tin[:6], tin[6:9], tin[9:17], tin[17])
    elif len(tin) == 15:
        return "{} {} {} (Old Regime)".format(tin[:5], tin[5:10], tin[10:15])
    return None

# GENERATION
#############

def generate(new_format=True):  # type: (bool) -> str
    """
    Generates a random valid Chinese TIN, either old (15-digit) or new (18-digit).
    """
    if new_format:
        base_number = "".join([str(randint(0, 9)) for _ in range(17)])
        check_digit = _calculate_digit(base_number)
        return base_number + check_digit
    else:
        return "".join([str(randint(0, 9)) for _ in range(15)])

# USAGE EXAMPLES
tin = generate()
print(f"Generated TIN: {format_tin(tin)} - Valid? {is_valid(tin)}")

tin_old = generate(new_format=False)
print(f"Generated TIN: {format_tin(tin_old)} - Valid? {is_valid(tin_old)}")

user_tin = input("Enter your TIN: ")
print(is_valid(user_tin))
print(f"Formatted TIN: {format_tin(user_tin)}")