# Exercício 3 - Seção 6.

# Programa responsável pela verificação de qual o combustível mais vendido em um posto.

# Definição de variáveis para a acumulação dos valores.
etanol = 0
gasolina = 0
diesel = 0

# Mensagem de apresentação do programa.
print("Controle de abastecimento")
print(" ")

# Mensagem informativa ao usuário.
print("1-Etanol")
print("2-Gasolina")
print("3-Diesel")
print("4-Fim")
print(" ")

# Inicialização de variável.
entrada = 0

# Definição de um loop while, execução enquanto o usuário não digitar 4.
while (entrada != 4):
    # Variável capturando a entrada de dados do usuário.
    entrada = int(input("Informe o tipo de combustível vendido: "))
    # Condicionais If/Else, controlando o fluxo de entrada do usuário.
    if (entrada == 1):
        etanol += 1
    elif (entrada == 2):
        gasolina += 1
    elif (entrada == 3):
        diesel += 1
    elif (entrada not in [1,2,3,4]):
        print("Entrada inválida")

# Saída dos dados.
print("Fim do expediente")
print(f"Quantidade de abastecimentos com Etanol: {etanol}")
print(f"Quantidade de abastecimentos com gasolina: {gasolina}")
print(f"Quantidade de abastecimentos com diesel: {diesel}")
print("Muito obrigado")
print("Fim do programa")
