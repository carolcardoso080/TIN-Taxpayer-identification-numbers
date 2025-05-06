from random import randint

# FORMATTING
#############

def remove_symbols(dirty_nif):  # type: (str) -> str
    """
    Removes spaces, dashes, and other symbols from a NIF.
    """
    return "".join(filter(str.isdigit, dirty_nif))

# VALIDATION
#############

def is_valid(nif):  # type: (str) -> bool
    """
    Validates a French NIF (Numéro d'Identification Fiscale) based on its structure.
    """
    nif = remove_symbols(nif)
    return len(nif) == 13 and nif.isdigit()

def is_valid_siren(siren):  # type: (str) -> bool
    """
    Validates a French SIREN number using the Luhn algorithm.
    """
    siren = remove_symbols(siren)
    return len(siren) == 9 and siren.isdigit() and _luhn_check(siren)

def is_valid_siret(siret):  # type: (str) -> bool
    """
    Validates a French SIRET number (9-digit SIREN + 5-digit NIC) using the Luhn algorithm.
    """
    siret = remove_symbols(siret)
    return len(siret) == 14 and siret.isdigit() and _luhn_check(siret)

# CHECK DIGIT CALCULATION
###########################

def _luhn_check(number):  # type: (str) -> bool
    """
    Validates a number using the Luhn algorithm (used for SIREN and SIRET).
    """
    total = 0
    reverse_digits = list(map(int, reversed(number)))
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0

def calculate_vat_control(siren):  # type: (str) -> str
    """
    Calculates the French VAT number control digits from a SIREN.
    """
    siren = remove_symbols(siren)
    if len(siren) != 9 or not siren.isdigit():
        return None
    control_digits = (12 + 3 * (int(siren) % 97)) % 97
    return f"FR{control_digits:02}{siren}"

def format_nif(nif):  # type: (str) -> str
    """
    Formats a French NIF for readability.
    """
    nif = remove_symbols(nif)
    if len(nif) != 13:
        return None
    return f"{nif[:3]} {nif[3:6]} {nif[6:9]} {nif[9:]}"

# GENERATION
#############

def generate_nif():  # type: () -> str
    """
    Generates a random valid French NIF (13 digits).
    """
    return str(randint(1000000000000, 9999999999999))

def generate_siren():  # type: () -> str
    """
    Generates a random valid French SIREN (9 digits, Luhn valid).
    """
    while True:
        siren = str(randint(100000000, 999999999))
        if _luhn_check(siren):
            return siren

def generate_siret():  # type: () -> str
    """
    Generates a random valid French SIRET (9-digit SIREN + 5-digit NIC, Luhn valid).
    """
    siren = generate_siren()
    nic = str(randint(10000, 99999))
    siret = siren + nic
    return siret if _luhn_check(siret) else generate_siret()

# USAGE EXAMPLES
nif = generate_nif()
print(f"Generated NIF: {format_nif(nif)} - Valid? {is_valid(nif)}")

siren = generate_siren()
print(f"Generated SIREN: {siren} - Valid? {is_valid_siren(siren)}")

siret = generate_siret()
print(f"Generated SIRET: {siret} - Valid? {is_valid_siret(siret)}")

vat = calculate_vat_control(siren)
print(f"Generated VAT: {vat}")

user_nif = input("Enter your NIF: ")
print(f"Valid? {is_valid(user_nif)}")
print(f"Formatted NIF: {format_nif(user_nif)}")