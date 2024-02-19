# Atribuição dos valores-verdade de A, B, e C
A = True
B = False
C = True

# Calcula o resultado da expressão not A or not( not B and C)
resultado = not A or not (not B and C)

# Imprime o resultado
print(f"O valor-verdade da expressão not A or not( not B and C) para A={A}, B={B} e C={C} é: {resultado}")
