from random import randint
from datetime import datetime

# FORMATTING
#############

def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes any non-digit characters from a Luxembourg tin.
    """
    return "".join(filter(str.isalnum, dirty_tin))


# VALIDATION
#############

def is_valid(tin):  # type: (str) -> bool
    """
    Validates a Luxembourg tin (matricule or VAT).
    """
    tin = remove_symbols(tin)

    if tin.startswith("LU") and len(tin) == 10:
        return _is_valid_vat(tin[2:])
    elif len(tin) == 13 and tin.isdigit():
        return _is_valid_matricule(tin)
    else:
        return False


def _is_valid_vat(vat_digits):  # type: (str) -> bool
    """
    Validates a Luxembourg VAT number using mod 89 check.
    """
    if len(vat_digits) != 8 or not vat_digits.isdigit():
        return False
    number = int(vat_digits[:6])
    check = int(vat_digits[6:])
    return number % 89 == check


def _is_valid_matricule(mat):  # type: (str) -> bool
    """
    Validates a 13-digit Matricule (no public check digit known).
    """
    try:
        datetime.strptime(mat[:8], "%Y%m%d")  # Check if date is valid
        return True
    except ValueError:
        return False


def format_tin(tin):  # type: (str) -> str
    """
    Formats a Luxembourg tin for readability.
    """
    tin = remove_symbols(tin)
    if tin.startswith("LU") and len(tin) == 10:
        return f"{tin[:2]} {tin[2:6]} {tin[6:]}"
    elif len(tin) == 13:
        return f"{tin[:4]}-{tin[4:6]}-{tin[6:8]} {tin[8:]}"
    return tin


# GENERATION
#############

def generate(type="vat"):  # type: (str) -> str
    """
    Generates a valid Luxembourg tin: either 'vat' or 'matricule'.
    """
    if type == "vat":
        base = randint(100000, 999999)
        check = base % 89
        return f"LU{base:06d}{check:02d}"
    elif type == "matricule":
        birth_date = datetime(randint(1900, 2020), randint(1, 12), randint(1, 28))
        date_str = birth_date.strftime("%Y%m%d")
        suffix = randint(10000, 99999)
        return f"{date_str}{suffix}"
    else:
        return None


# USAGE EXAMPLES
tin_vat = generate("vat")
tin_mat = generate("matricule")

print(f"Generated VAT tin: {format_tin(tin_vat)} - Valid? {is_valid(tin_vat)}")
print(f"Generated Matricule: {format_tin(tin_mat)} - Valid? {is_valid(tin_mat)}")

user_tin = input("Enter your Luxembourg tin (matricule or VAT): ")
print(f"Valid? {is_valid(user_tin)}")
print(f"Formatted tin: {format_tin(user_tin)}")