# Programa responsável pela leitura de um determinado número, retornando todos os seus divisores.

# Mensagens de apresentação e instruções de uso
print("Verificador de divisores")
valor_x = int(input("Informe um número inteiro qualquer: "))
print(f"Os divisores de {valor_x} são: ")

# Loop for com if aninhado solucionando o problema.
for i in range(valor_x, 0, -1):
    if (valor_x % i == 0):
        print(i)

# Mensagens do fim do programa.
print("-----------------------------")
print("Fim do programa")
