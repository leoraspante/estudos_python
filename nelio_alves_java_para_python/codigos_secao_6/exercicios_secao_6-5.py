# Exercício 5 - Seção 6.

# Código onde verificamos se um determinado valor digitado pelo usuário está ou não dentro de um intervalo estabelecido.
# A quantidade de verificações será também definida pelo usuário.

print("Verificador de intervalo")
print(" ")
print("Quantas verificações deseja realizar?")
qtd_iteracoes = int(input("Informe um valor inteiro: "))
print(" ")
print("Informe a seguir os valores que deseja verificar: ")

print(" ")

# Definição de variáveis acumuladoras.
values_in = 0
values_out = 0

for i in range (qtd_iteracoes):
    valor_X = int(input("Digite um número inteiro qualquer: "))
    if (valor_X >= 10 and valor_X <= 20):
        values_in += 1
    else:
        values_out += 1

# Mensagem de saída.
print(" ")
print("Resultados:")
print(f"Valores dentro do intervalo: {values_in}")
print(f"Valores fora do intervalo: {values_out}")
print("-----------------------------")
print("Fim do programa")
