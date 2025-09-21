# Programa onde será realizado o cálculo de fatorial de um determinado valor informado pelo usuário.

# Mensagem de apresentação do programa e instruções de uso.
print("Calculadora Fatorial")
print("Informe um valor inteiro qualquer para calcular seu fatorial")
valor_x = int(input("Digite um número inteiro qualquer: "))

# Declaração de variável para acumular o valor da fatorial.
fatorial = 1

# Declaração de um If/Else para uma verificação inicial.
if (valor_x == 0):
    print(" ")
    print(f"O fatorial de {valor_x} é: 1.")
    print("----------------------------")
    print("Fim do programa")

else:
    for i in range(valor_x, 0, -1): # começa em valor_x, termina antes de 0, e decrementa de 1 em 1.
        fatorial *= i
    print(" ")
    print(f"O fatorial de {valor_x} é: {fatorial}.")
    print("----------------------------")
    print("Fim do programa")

