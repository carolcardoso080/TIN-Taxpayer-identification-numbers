from random import choice, randint
from datetime import datetime
import string

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes any non-alphanumeric characters from a Mexican tin.
    """
    return "".join(filter(str.isalnum, dirty_tin.upper()))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Mexican tin based on length and structure.
    Does not validate the official SAT checksum.
    """
    tin = remove_symbols(tin)
    if len(tin) == 13:
        return tin[:4].isalpha() and tin[4:10].isdigit() and tin[10:].isalnum()
    elif len(tin) == 12:
        return tin[:3].isalpha() and tin[3:9].isdigit() and tin[9:].isalnum()
    return False


# TYPE IDENTIFICATION
########################

def get_tin_type(tin):  # type: (str) -> str
    """
    Identifies if the tin belongs to an individual or a company.
    """
    tin = remove_symbols(tin)
    if len(tin) == 13:
        return "individual"
    elif len(tin) == 12:
        return "company"
    return "unknown"


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Mexican tin for readability.
    """
    tin = remove_symbols(tin)
    if len(tin) == 13:
        return f"{tin[:4]}-{tin[4:10]}-{tin[10:]}"
    elif len(tin) == 12:
        return f"{tin[:3]}-{tin[3:9]}-{tin[9:]}"
    return tin


# GENERATION
#############

def generate(tin_type="individual"):  # type: (str) -> str
    """
    Generates a random valid Mexican tin for individuals or companies.
    """
    if tin_type == "individual":
        prefix = ''.join(choice(string.ascii_uppercase) for _ in range(4))
        birth_date = datetime(randint(1950, 2005), randint(1, 12), randint(1, 28))
        date_str = birth_date.strftime("%y%m%d")
        suffix = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(3))
        return prefix + date_str + suffix
    elif tin_type == "company":
        prefix = ''.join(choice(string.ascii_uppercase) for _ in range(3))
        creation_date = datetime(randint(1950, 2022), randint(1, 12), randint(1, 28))
        date_str = creation_date.strftime("%y%m%d")
        suffix = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(3))
        return prefix + date_str + suffix
    return None


# USAGE EXAMPLES
tin_ind = generate("individual")
tin_cmp = generate("company")

print(f"Generated Individual tin: {format_tin(tin_ind)} - Valid? {is_valid(tin_ind)} - Type: {get_tin_type(tin_ind)}")
print(f"Generated Company tin: {format_tin(tin_cmp)} - Valid? {is_valid(tin_cmp)} - Type: {get_tin_type(tin_cmp)}")

user_tin = input("Enter your Mexican tin: ")
print(f"Valid? {is_valid(user_tin)} - Type: {get_tin_type(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")
