# Exercício 1 - Sessão 5.

# Mensagem de apresentação do programa.
print("Bem vindo ao NumCheck !.")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
valor_a = float (input("Digite um número qualquer: "))

# Condicional responsável pela verificação do número.
if (valor_a < 0): # Checa se o número é negativo.
    print(f"O número {valor_a} é um número negativo.")
else:
    print(f"O número {valor_a} é um número positivo.")

