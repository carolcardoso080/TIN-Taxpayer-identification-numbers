from random import randint

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes any non-digit characters from a Dutch tin (BSN/RSIN).
    """
    return "".join(filter(str.isdigit, dirty_tin))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Dutch BSN or RSIN number using the Elfproef (mod 11 check).
    """
    tin = remove_symbols(tin)
    if len(tin) != 9 or not tin.isdigit():
        return False
    return _elfproef(tin)


# CHECK DIGIT CALCULATION
###########################

def _elfproef(tin):  # type: (str) -> bool
    """
    Performs the Elfproef (mod 11) check on a 9-digit Dutch number.
    """
    weights = list(range(9, 1, -1)) + [-1]
    total = sum(int(d) * w for d, w in zip(tin, weights))
    return total % 11 == 0


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Dutch tin (BSN/RSIN) for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) != 9:
        return None
    return f"{tin[:3]}.{tin[3:6]}.{tin[6:]}"


# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a valid Dutch BSN/RSIN number.
    """
    while True:
        tin = str(randint(100000000, 999999999))
        if _elfproef(tin):
            return tin


# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your Dutch tin (BSN or RSIN): ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")