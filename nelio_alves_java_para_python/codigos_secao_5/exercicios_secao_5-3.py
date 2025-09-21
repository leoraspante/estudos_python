# Exercício 3 - Seção 5.

# Mensagem de apresentação do programa.
print("Bem vindo ao NumCheck 3.0 !.")
print("Agora verificamos se os números digitados são múltiplos. ")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
valor_a = float (input("Digite um número qualquer: "))
valor_b = float (input("Digite outro número qualquer: "))

# Condicional responsável pela verificação do número.
if (valor_a % valor_b == 0) or (valor_b % valor_a == 0): # Checa se o número é par
    print(f"O número {valor_a} e o número {valor_b} são múltiplos.")
else:
    print(f"O número {valor_a} e o número {valor_b} não são múltiplos.")