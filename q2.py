def encontra_k(numero):
    k = (numero - 1) // 2
    print(f"O número {numero} pode ser escrito na forma 2k + 1 como (2 * {k} + 1) = {2*k + 1}, onde k = {k}.")


def calcula_quadrado(numero):
    quadrado = numero ** 2
    k_quadrado = ((quadrado - 1) // 2)
    print(f"O quadrado de {numero} é {quadrado}, que pode ser escrito na forma 2k + 1 como (2 * {k_quadrado} + 1) = {2*k_quadrado + 1}, onde k = {k_quadrado}.")


# Verifica se o número é ímpar
def verifica_impar(numero):
    if numero % 2 != 0:
        return True
    else:
        return False


# Lê um número do teclado e verifica se é ímpar
numero = int(input("Digite um número ímpar: "))
if verifica_impar(numero):
    # Escreve o número na forma 2k + 1
    encontra_k(numero)
    # Calcula o quadrado do número e escreve na forma 2k + 1
    calcula_quadrado(numero)
else:
    print("O número digitado não é ímpar.")
