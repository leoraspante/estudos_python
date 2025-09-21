# Exercício 7 - Seção 5.

# Mensagem de apresentação do programa.
print("Indicador de coordenadas")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
valor_x = float (input("Informe o valor de X: "))
valor_y = float (input("Informe o valor de Y: "))
print(" ")

# Condicionais de verificação
if (valor_x == 0 and valor_y == 0): # Condição de origem.
    print("O ponto está na origem.")

elif (valor_x == 0): # Ponto sobre eixo Y.
    print("O ponto está sobre o eixo Y.")

elif (valor_y == 0): # Ponto sobre eixo X.
    print("O ponto está sobre o eixo X.")

elif (valor_x > 0 and valor_y > 0): # Ponto sobre Q1.
    print("O ponto está sobre o Q1.")

elif (valor_x < 0 and valor_y > 0): # Ponto sobre Q2.
    print("O ponto está sobre o Q2.")

elif (valor_x < 0 and valor_y < 0): # Ponto sobre Q3.
    print("O ponto está sobre o Q3.")

elif (valor_x > 0 and valor_y < 0): # Ponto sobre Q4.
    print("O ponto está sobre o Q4.")
