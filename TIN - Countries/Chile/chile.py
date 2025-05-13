from random import randint

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes dots, dashes, and spaces from a Chilean tin.
    """
    return "".join(filter(str.isalnum, dirty_tin)).upper()

# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Chilean tin based on its check digit.
    """
    tin = remove_symbols(tin)
    if len(tin) < 2 or not tin[:-1].isdigit():
        return False
    base = tin[:-1]
    dv = tin[-1]
    return _calculate_digit(base) == dv

# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> str
    """
    Calculates the check digit for a Chilean tin base.
    """
    reversed_digits = list(map(int, reversed(base)))
    factors = [2, 3, 4, 5, 6, 7]
    total = sum(d * factors[i % 6] for i, d in enumerate(reversed_digits))
    remainder = 11 - (total % 11)
    if remainder == 11:
        return '0'
    elif remainder == 10:
        return 'K'
    else:
        return str(remainder)

def format_tin(tin):  # type: (str) -> str
    """
    Formats a Chilean tin for readability (XX.XXX.XXX-D).
    """
    tin = remove_symbols(tin)
    if len(tin) < 2:
        return None
    number = tin[:-1]
    dv = tin[-1]
    number = number.zfill(8)
    return f"{number[:-6]}.{number[-6:-3]}.{number[-3:]}-{dv}"

# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a valid Chilean tin.
    """
    base = str(randint(1000000, 25000000))
    dv = _calculate_digit(base)
    return base + dv

# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your tin: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")