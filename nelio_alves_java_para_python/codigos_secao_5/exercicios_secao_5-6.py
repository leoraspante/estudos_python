# Exercício 6 - Seção 5.

# Mensagem de apresentação do programa.
print("Identificador de intervalo.")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
numero = float (input("Informe um valor qualquer: "))

# Condicional responsável pela verificação do tempo de jogo.
if (numero >= 0 and numero <= 25): # Intervalo [0,25].
    print(f"O valor digitado {numero} está entre o intervalo: [0,25].")

elif (numero > 25 and numero <= 50): # Intervalo (25,50].
    print(f"O valor digitado {numero} está entre o intervalo: (25,50].")

elif (numero > 50 and numero <= 75): # Intervalo (50,75].
    print(f"O valor digitado {numero} está entre o intervalo: (50,75].")

elif (numero > 75 and numero <= 100): # Intervalo (75,100].
    print(f"O valor digitado {numero} está entre o intervalo: (75,100].")

else: # Fora do intervalo
    print(f"O valor digitado {numero} está fora do intervalo.")