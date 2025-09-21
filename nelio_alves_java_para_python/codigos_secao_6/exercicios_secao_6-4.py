# Exercício 4 - Seção 6.

# Código simples para a verificação de valores ímpares em um determinado intervalo, fazendo uso do loop for.

# Mensagem de apresentação e instrução de uso.
print("Verificador de ímpares")
print(" ")
value_X = int(input("Informe um valor inteiro qualquer: "))
print(" ")
print(f"Todos os ímpares até: {value_X}")

# Loop for criado para iterar até o valor digitado pelo usuário
for i in range (value_X + 1):
    if (i % 2 != 0): # If realizando a verificação de cada número.
        print(i)
print("---------------------------------------")
print("Fim do programa")