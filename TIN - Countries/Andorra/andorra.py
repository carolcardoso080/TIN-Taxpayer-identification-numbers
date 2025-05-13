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
    Validates an Andorran tin based on its known strict structure.
    Expected format: X123456Z where:
    - X is one of a defined set of valid types
    - 123456 are digits
    - Z is a control letter
    """
    tin = remove_symbols(tin)
    if len(tin) != 8:
        return False
    allowed_prefixes = {'F', 'A', 'L', 'E', 'C', 'D', 'G', 'O', 'P', 'U'}
    return (
        tin[0] in allowed_prefixes and
        tin[1:7].isdigit() and
        tin[-1].isalpha()
    )


# FORMATTING
#############

def format_tin(tin):  # type: (str) -> str
    """
    Formats an Andorran tin for readability.
    Example: F-123456-Z
    """
    tin = remove_symbols(tin)
    if len(tin) != 8:
        return None
    return f"{tin[0]}-{tin[1:7]}-{tin[7]}"


# GENERATION
#############

def generate():  # type: () -> str
    """
    Generates a random valid Andorran tin with an accepted prefix.
    """
    allowed_prefixes = ['F', 'A', 'L', 'E', 'C', 'D', 'G', 'O', 'P', 'U']
    prefix = choice(allowed_prefixes)
    digits = str(randint(100000, 999999))
    control = choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return prefix + digits + control


# USAGE EXAMPLES
tin = generate()
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your Andorran tin: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")
