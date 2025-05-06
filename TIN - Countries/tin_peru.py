from random import randint, choice

# FORMATTING
#############

def remove_symbols(dirty_ruc):  # type: (str) -> str
    """
    Removes spaces, dashes, and other symbols from a RUC.
    """
    return "".join(filter(str.isdigit, dirty_ruc))

# VALIDATION
#############

def is_valid(ruc):  # type: (str) -> bool
    """
    Validates a Peruvian RUC based on its structure and check digit.
    """
    ruc = remove_symbols(ruc)
    if len(ruc) != 11 or ruc[:2] not in ['10', '20', '15', '16', '17']:
        return False
    base, check_digit = ruc[:-1], int(ruc[-1])
    return _calculate_digit(base) == check_digit

# CHECK DIGIT CALCULATION
###########################

def _calculate_digit(base):  # type: (str) -> int
    """
    Calculates the check digit for a given RUC base using modulo 11.
    """
    weights = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    total = sum(int(d) * w for d, w in zip(base, weights))
    remainder = total % 11
    check_digit = 11 - remainder
    return 0 if check_digit == 10 else check_digit

def format_ruc(ruc):  # type: (str) -> str
    """
    Formats a Peruvian RUC for readability.
    """
    ruc = remove_symbols(ruc)
    if len(ruc) != 11:
        return None
    return "{}.{}.{}/{}".format(ruc[:2], ruc[2:5], ruc[5:10], ruc[10])

# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a random valid Peruvian RUC.
    """
    prefix = choice(['10', '20', '15', '16', '17'])
    base_number = str(randint(10000000, 99999999))  # Ensure 8-digit base
    base = prefix + base_number
    check_digit = _calculate_digit(base)
    return base + str(check_digit)

# USAGE EXAMPLES
ruc = generate()
print(f"Generated RUC: {format_ruc(ruc)} - Valid? {is_valid(ruc)}")

user_ruc = input("Enter your RUC: ")
print(is_valid(user_ruc))
print(f"Formatted RUC: {format_ruc(user_ruc)}")