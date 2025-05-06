from random import randint, choice
import string

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes non-alphanumeric characters from the tin number.
    """
    return "".join(filter(str.isalnum, dirty_tin.upper()))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates an Irish tin number based on check digit rules.
    """
    tin = remove_symbols(tin)
    if len(tin) not in [8, 9] or not tin[:7].isdigit() or not tin[7].isalpha():
        return False

    total = sum(int(d) * w for d, w in zip(tin[:7], range(8, 1, -1)))
    if len(tin) == 9:
        # 9th character contributes a weight of 9
        total += (ord(tin[8]) - 64) * 9  # A=1

    remainder = total % 23
    expected_letter = chr(remainder + 64) if remainder != 0 else 'W'
    return tin[7] == expected_letter


def format_tin(tin):  # type: (str) -> str
    """
    Formats a tin number for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) == 8:
        return f"{tin[:7]}-{tin[7]}"
    elif len(tin) == 9:
        return f"{tin[:7]}-{tin[7]}{tin[8]}"
    return tin


# GENERATION
#############

def generate(include_ninth=False):  # type: (bool) -> str
    """
    Generates a valid Irish tin number.
    """
    digits = str(randint(1000000, 9999999))
    total = sum(int(d) * w for d, w in zip(digits, range(8, 1, -1)))
    remainder = total % 23
    check_letter = chr(remainder + 64) if remainder != 0 else 'W'

    if include_ninth:
        extra_letter = choice(string.ascii_uppercase)
        total += (ord(extra_letter) - 64) * 9
        return digits + check_letter + extra_letter
    return digits + check_letter


# USAGE EXAMPLES
tin = generate(include_ninth=True)
print(f"Generated tin: {format_tin(tin)} - Valid? {is_valid(tin)}")

user_tin = input("Enter your tin number: ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")