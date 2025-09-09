# Exercício 2 - Sessão 5.

# Mensagem de apresentação do programa.
print("Bem vindo ao NumCheck 2.0 !.")
print("Agora verificamos se o número é par ou ímpar. ")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
valor_a = float (input("Digite um número qualquer: "))

# Condicional responsável pela verificação do número.
if (valor_a % 2 == 0): # Checa se o número é par
    print(f"O número {valor_a} é um número par.")
else:
    print(f"O número {valor_a} é um número ímpar.")