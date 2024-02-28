from sympy import symbols, expand, binomial

# Define las variables
a, b, n = symbols('a b n')

# Define el binomio (a + b)^n
binomial_expression = binomial(a + b, n)

# Expande el binomio
expanded_expression = expand(binomial_expression)

# Imprime el resultado
print(expanded_expression)