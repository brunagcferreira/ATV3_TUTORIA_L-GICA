
# Recebe os números pares n e p
n = int(input("Digite um número par (n): "))
p = int(input("Digite outro número par (p): "))

# Verifica se n e p são pares
if n % 2 != 0 or p % 2 != 0:
    print("Os números informados não são pares. Por favor, insira números pares.")
else:
    # Encontra as variáveis k e y
    k = n // 2
    y = p // 2

    # Imprime no formato n = 2k1 e p = 2k2
    print(f"n = 2*{k} = {n}")
    print(f"p = 2*{y} = {p}")

    # Calcula o produto n*p
    produto = n * p
    print(f"Produto n*p = {produto}")

    # Encontra a variável x
    x = produto // 2

    # Imprime no formato n*p = 2k
    print(f"n*p = 2*{x} = {produto}")
