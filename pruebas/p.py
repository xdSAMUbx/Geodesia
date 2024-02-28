from sympy import symbols, sqrt, series

x = symbols('x')
expr = sqrt(1 - x**2)

taylor_series = series(expr, x, n=5).removeO()

print(taylor_series)