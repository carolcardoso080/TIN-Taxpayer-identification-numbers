# TIN-Taxpayer-identification-numbers

<div align="center">
<h1>TIN - Taxpayer identification numbers</h1>

<p>Library of tax identification numbers of the countries of the world</p>

### [Procurando pela versão em português (PT-BR)?](README.md)

</div>

# Introduction

TIN Taxpayer identification numbers is a library focused on solving problems that we face daily in the development of applications with analysis and validation of tax numbers, which vary from country to country, both for individuals and legal entities.

- [Installation](#installation)
- [Usage](#usage)
- [Utilities](#utilities)

# Installation

```
testtests
```

# Usage

To use one of our utilities, simply import the required function, as in the example below:

```
testtests
```

# Utilities

- [Angola](#angola)
- [is\_valid\_cpf](#is_valid)
- [format\_tin](#format_tin)
- [remove\_symbols](#remove_symbols)
- [generate](#generate)

## CPF

### is_valid

Returns whether the verification digits of the provided CPF
match its base number. This function does not verify the existence of the CPF;
it only validates the format of the string.

Arguments:

- cpf (str): The CPF to be validated, an 11-digit string

Returns:

- bool: True if the check digits match the base number,
False otherwise.

Example:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf("82178537464")
True
>>> is_valid_cpf('00011122233')
False
```

### format_tin

Formats a CPF (Brazilian Individual Taxpayer Registry) for visual display.

This function takes a CPF string containing only numbers as input and
adds standard formatting symbols for display.

Arguments:

- cpf (str): A CPF string containing only numbers.

Returns:

- str: The CPF formatted with visual symbols if valid,
None if not.

Example:

```python
>>> from brutils import format_cpf
>>> format_cpf('82178537464')
'821.785.374-64'
>>> format_cpf("55550207753")
'555.502.077-53'
```

### remove_symbols

Removes specific symbols from a CPF (Brazilian Individual Taxpayer Registry) string. This function receives as input a CPF string and removes all
occurrences of the characters '.', '-' from it.

Arguments:

- cpf (str): The CPF string containing the symbols to be removed.

Returns:

- str: A new string with the specified symbols removed.

Example:

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate

Generate a random string of valid CPF digits.

Returns:

- str: A randomly generated valid CPF.

Example:

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
>>> generate_cpf()
"10895948109"
```
