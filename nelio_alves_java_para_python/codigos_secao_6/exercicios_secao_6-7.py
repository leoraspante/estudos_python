# Exercício 7 - Seção 6.

# Programa que realiza a leitura de dois valores e retorna o resultado da divisão.
# A quantidade de divisões a serem realizadas é definida pelo usuário.
# A divisão de valores por zero, retorna uma mensagem de advertência.

# Mensagem de apresentação e instruções de uso.
print("Divisor de valores inteiros")
print("Informe quantas divisões deseja realizar")
qtd_operacoes = int(input("Digite um número inteiro qualquer: "))
print(" ")

# Definição do loop for.
for i in range(qtd_operacoes):
    print(f"{i+1}ª Operação")
    valor_x = int(input("Digite o valor de X: "))
    valor_y = int(input("Digite o valor de Y: "))
    if (valor_y == 0):
        print("Não é possível dividir por zero.")
        print(" ")
    else:
        resultado = valor_x/valor_y
        print(f"O resultado da divisão é: {resultado:.2f}")
        print(" ")

# Mensagem de encerramento.
print("-----------------------------")
print("Fim do programa")