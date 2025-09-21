# Exercício 2 - Seção 4.

# Mensagem de apresentação do programa.
print("Bem vindo ao Círculo Precision.")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
valor_x = float (input("Informe o raio do círculo: "))

# Variável armazendando o valor de pi.
pi = 3.14159

# Variavel responsável pelo cálculo de área do círculo.
resultado = pi * (valor_x**2)

# Exibição do resultado.
print(f"A área do círculo é: {resultado:.4f}.")
