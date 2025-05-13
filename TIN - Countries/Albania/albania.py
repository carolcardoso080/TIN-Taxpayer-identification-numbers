from random import randint, choice

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes non-alphanumeric characters from the tin.
    """
    return "".join(filter(str.isalnum, dirty_tin.upper()))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates an Albanian tin by format and check character.
    """
    tin = remove_symbols(tin)
    if len(tin) != 10:
        return False
    if not (tin[0].isalpha() and tin[-1].isalpha()):
        return False
    if not tin[1:9].isdigit():
        return False
    return True  # Format validation only; actual check character algorithm is not public


# FORMATTING
#############

def format_tin(tin):  # type: (str) -> str
    """
    Formats an Albanian tin for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) != 10:
        return None
    return f"{tin[0]}-{tin[1:4]}-{tin[4:7]}-{tin[7:9]}-{tin[9]}"


# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a random valid Albanian tin.
    """
    first_letter = choice('JKL')  # Types of entities
    digits = str(randint(10000000, 99999999))
    last_letter = choice('ABCDEFGHJKLMNPQRSTUVWXYZ')  # Random valid control character
    return first_letter + digits + last_letter


# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your Albanian tin: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")
