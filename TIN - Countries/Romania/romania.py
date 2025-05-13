from random import randint, choice

# REMOVE SYMBOLS
def remove_symbols(dirty_tin):  # type: (str) -> str
    """
    Removes spaces, dots, dashes, and other symbols from a string.
    """
    return "".join(filter(str.isdigit, dirty_tin))


def is_valid(tin):
    tin = remove_symbols(tin)

    if len(tin) != 13 or not tin.isdigit():
        return "Invalid tin: Must contain exactly 13 numeric digits."

    expected_control_digit = calculate(tin[:-1])
    if tin[-1] != expected_control_digit:
        return "Invalid tin: Incorrect check digit."

    return "Valid tin"

# WEIGHTS FOR CALCULATION OF THE CHECK DIGIT
WEIGHTS = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

def calculate(tin_without_control):
    total = sum(int(tin_without_control[i]) * WEIGHTS[i] for i in range(12))
    remainder = total % 11
    return "1" if remainder == 10 else str(remainder)

def generate():
    S = str(randint(1, 6))  # Gender and century
    YY = str(randint(0, 99)).zfill(2)  # Year of birth
    MM = str(randint(1, 12)).zfill(2)  # Month of birth
    DD = str(randint(1, 28)).zfill(2)  # Birth date (simplified to 28)
    JJ = str(randint(1, 52)).zfill(2)  # District code
    NNN = str(randint(1, 999)).zfill(3)  # Unique number
    partial_tin = S + YY + MM + DD + JJ + NNN
    C = calculate(partial_tin)  # Cálculo do dígito de controle
    return partial_tin + C

def format_tin(tin):
    tin = remove_symbols(tin)
    if len(tin) != 13:
        return None
    return f"{tin[:1]}-{tin[1:3]}{tin[3:5]}{tin[5:7]}-{tin[7:9]}-{tin[9:12]}-{tin[12]}"

def example_usage():
    generated_tin = generate()
    print(f"Generated tin: {generated_tin} - Valid? {is_valid(generated_tin)}")

    user_input = input("Enter your tin: ")
    print(is_valid(user_input))

    formatted_tin = format_tin(user_input)
    if formatted_tin:
        print(f"Formatted tin: {formatted_tin}")

# Run example
example_usage()
