from random import randint, choice

# REMOVE FORMATTING
def remove_symbols(dirty_tin):
    """Removes spaces, dots, and dashes from the NIF."""
    return "".join(filter(str.isdigit, dirty_tin))

# VALIDATE CÉDULA
def is_valid_cedula(cedula):
    """Validates a Cédula de Identidad."""
    cedula = remove_symbols(cedula)
    if len(cedula) != 11 or not cedula.isdigit():
        return "Invalid Cédula: Must contain exactly 11 numeric digits."
    expected_control_digit = calculate_cedula_control_digit(cedula[:-1])
    return "Valid Cédula." if cedula[-1] == expected_control_digit else "Invalid Cédula: Incorrect control digit."

# VALIDATE tin
def is_valid_tin(tin):
    """Validates an tin."""
    tin = remove_symbols(tin)
    if len(tin) != 9 or not tin.isdigit():
        return "Invalid tin: Must contain exactly 9 numeric digits."
    expected_control_digit = calculate_tin_control_digit(tin[:-1])
    return "Valid tin." if tin[-1] == expected_control_digit else "Invalid tin: Incorrect control digit."

# CONTROL DIGIT CALCULATION (MODULO 10 - CÉDULA)
def calculate_cedula_control_digit(tin):
    """Calculates the control digit for the Cédula using the Luhn Algorithm."""
    total = 0
    reversed_digits = list(map(int, tin[::-1]))
    for i, digit in enumerate(reversed_digits):
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return str((10 - (total % 10)) % 10)

# CONTROL DIGIT CALCULATION (MODULO 11 - tin)
def calculate_tin_control_digit(tin):
    """Calculates the control digit for tin using Modulo 11."""
    weights = [7, 9, 8, 6, 5, 4, 3, 2]
    total = sum(int(tin[i]) * weights[i] for i in range(8))
    remainder = total % 11
    return "0" if remainder == 10 else str(11 - remainder)

# FORMAT CÉDULA FOR DISPLAY
def format_cedula(cedula):
    """Formats the Cédula for display."""
    cedula = remove_symbols(cedula)
    if len(cedula) != 11:
        return None
    return f"{cedula[:3]}-{cedula[3:10]}-{cedula[10]}"

# FORMAT tin FOR DISPLAY
def format_tin(tin):
    """Formats the tin for display."""
    tin = remove_symbols(tin)
    if len(tin) != 9:
        return None
    return f"{tin[:1]}-{tin[1:9]}-{tin[9]}"

# GENERATE VALID CÉDULA
def generate_cedula():
    """Generates a valid Cédula de Identidad."""
    province_code = str(randint(1, 999)).zfill(3)
    sequential_tin = str(randint(1, 9999999)).zfill(7)
    partial_cedula = province_code + sequential_tin
    control_digit = calculate_cedula_control_digit(partial_cedula)
    return f"{province_code}-{sequential_tin}-{control_digit}"

# GENERATE VALID tin
def generate_tin():
    """Generates a valid tin."""
    entity_type = str(randint(1, 3))  # 1 for private company, 2 for government, 3 for NGOs
    sequence_tin = str(randint(1, 99999999)).zfill(8)
    partial_tin = entity_type + sequence_tin
    control_digit = calculate_tin_control_digit(partial_tin)
    return f"{entity_type}-{sequence_tin}-{control_digit}"


# EXAMPLES OF USAGE
def example_usage():
    generated_cedula = generate_cedula()
    print(f"Generated Cédula: {generated_cedula} - Valid? {is_valid_cedula(generated_cedula)}")

    generated_tin = generate_tin()
    print(f"Generated tin: {generated_tin} - Valid? {is_valid_tin(generated_tin)}")

    user_input = input("Enter your Cédula or tin: ")
    if len(user_input) == 11:
        print(is_valid_cedula(user_input))
        print(f"Formatted Cédula: {format_cedula(user_input)}")
    elif len(user_input) == 9:
        print(is_valid_tin(user_input))
        print(f"Formatted tin: {format_tin(user_input)}")

# Run example
example_usage()