# Exercício 6 - Sessão 4.

# Mensagem de apresentação do programa.
print("Combined Calculator.")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
valor_a = float (input("Informe o valor de A: "))
valor_b = float (input("Informe o valor de B: "))
valor_c = float (input("Informe o valor de C: "))

# Variável responsável pelo cálculo de área do triângulo.
triangulo = (valor_a * valor_c) / 2

# Variável responsável pelo cálculo de área do círculo.
pi = 3.14159
potencia_c = valor_c ** 2
circulo = pi * potencia_c

# Variável responsável pelo cálculo de área do trapézio.
trapezio = ((valor_a + valor_b) * valor_c) / 2

# Variavel responsável pelo cálculo do quadrado.
quadrado = valor_b ** 2

# Variavel responsável pelo cálculo do retângulo.
retangulo = valor_a * valor_b

# Exibição do resultado.
print(f"Área do triângulo: {triangulo:.3f}.")
print(f"Área do círculo: {circulo:.3f}.")
print(f"Área do trapézio: {trapezio:.3f}.")
print(f"Área do quadrado: {quadrado:.3f}.")
print(f"Área do retângulo: {retangulo:.3f}.")