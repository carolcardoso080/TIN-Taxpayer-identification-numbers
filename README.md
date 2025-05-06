# TIN-Taxpayer-identification-numbers

<div align="center">
<h1>TIN - Taxpayer identification numbers</h1>

<p>Biblioteca de números de identificação fiscal dos países do mundo</p>

### [Looking for the english version?](README_EN.md)

</div>

# Introdução

TIN Taxpayer identification numbers é uma biblioteca com foco na resolução de problemas que enfrentamos diariamente no
desenvolvimento de aplicações com análise e validação de números fiscais, que variam de país para país, tanto de pessoas físicas quanto jurídicas.

- [Instalação](#instalação)
- [Utilização](#utilização)
- [Utilitários](#utilitários)

# Instalação

```
testestestes
```

# Utilização

Para usar um de nossos utilitários, basta importar a função necessária, como no exemplo abaixo:

```
testestestes
```

# Utilitários

- [Angola](#angola)
  - [is\_valid\_cpf](#is_valid)
  - [format\_tin](#format_tin)
  - [remove\_symbols](#remove_symbols)
  - [generate](#generate)

## CPF

### is_valid

Retorna se os dígitos de verificação do CPF fornecido
correspondem ao seu número base. Esta função não verifica a existência do CPF;
ela apenas valida o formato da string.

Argumentos:

- cpf (str): O CPF a ser validado, uma string de 11 dígitos

Retorna:

- bool: Verdadeiro se os dígitos de verificação corresponderem ao número base,
          Falso caso contrário.

Exemplo:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf("82178537464")
True
>>> is_valid_cpf('00011122233')
False
```

### format_tin

Formata um CPF (Cadastro de Pessoa Física brasileiro) para exibição visual.
Esta função recebe uma string de CPF contendo apenas números como entrada e
adiciona símbolos de formatação padrão para exibição.

Argumentos:

- cpf (str): Uma string de CPF contendo apenas números.

Retorna:

- str: O CPF formatado com símbolos visuais se for válido,
         None se não for válido.

Exemplo:

```python
>>> from brutils import format_cpf
>>> format_cpf('82178537464')
'821.785.374-64'
>>> format_cpf("55550207753")
'555.502.077-53'
```

### remove_symbols

Remove símbolos específicos de uma string de CPF (Cadastro de Pessoa Física
brasileiro). Esta função recebe como entrada uma string de CPF e remove todas as
ocorrências dos caracteres '.', '-' dela.

Argumentos:

- cpf (str): A string de CPF contendo os símbolos a serem removidos.

Retorna:

- str: Uma nova string com os símbolos especificados removidos.

Exemplo:

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate

Gerar uma string de dígitos de CPF válida aleatória.

Retorna:

- str: Um CPF válido gerado aleatoriamente.

Exemplo:

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
>>> generate_cpf()
"10895948109"
```
