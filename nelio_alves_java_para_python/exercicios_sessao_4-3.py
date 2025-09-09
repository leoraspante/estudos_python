# Exercício 3 - Sessão 4.

# Mensagem de apresentação do programa.
print("Calculadora de diferença.")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
valor_A = float (input("Digite o valor de A: "))
valor_B = float (input("Digite o valor de B: "))
valor_C = float (input("Digite o valor de C: "))
valor_D = float (input("Digite o valor de D: "))

# Variavel responsável pelo cálculo da diferença.
resultado = (valor_A * valor_B) - valor_C * valor_D

# Exibição do resultado.
print(f"A diferença dos valores é igual a: {resultado}.")
