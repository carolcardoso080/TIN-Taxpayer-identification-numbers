from random import randint

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes non-digit characters from the TIN.
    """
    return "".join(filter(str.isdigit, dirty_tin))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Syrian TIN (9-digit number with check digit).
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
    Calculates the check digit using modulus 11 algorithm.
    """
    weights = list(range(9, 1, -1))  # Weights from 9 to 2
    total = sum(int(d) * w for d, w in zip(base, weights))
    remainder = total % 11
    check = 11 - remainder
    return check if check < 10 else 0


# FORMATTING FOR DISPLAY
##########################

def format_tin(tin):  # type: (str) -> str
    """
    Formats the TIN into groups of 3 digits.
    """
    tin = remove_symbols(tin)
    if len(tin) != 9:
        return tin
    return f"{tin[:3]}-{tin[3:6]}-{tin[6:]}"


# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a valid Syrian TIN (9-digit number).
    """
    base = str(randint(10000000, 99999999))  # 8 digits
    check_digit = _calculate_digit(base)
    return base + str(check_digit)


# USAGE EXAMPLES
tin = generate()
print(f"Generated TIN: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your Syrian TIN: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted TIN: {format_tin(user_tin)}")
