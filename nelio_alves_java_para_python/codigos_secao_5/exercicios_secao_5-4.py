# Exercício 4 - Sessão 5.

# Mensagem de apresentação do programa.
print("Bem vindo ao Tempo de Jogatina !.")
print("Gerenciando seu tempo de jogo. ")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
inicio = float (input("Início da jogatina: "))
termino = float (input("Final da jogatina: "))

# Condicional responsável pela verificação do tempo de jogo.
if (inicio >= termino): # Checa se o horário de início é maior ou igual ao horário de término.
    tempo = (24 - inicio) + termino
    print(f"Você jogou por: {tempo} horas.")
else:
    tempo = termino - inicio
    print(f"Você jogou por: {tempo} horas.")