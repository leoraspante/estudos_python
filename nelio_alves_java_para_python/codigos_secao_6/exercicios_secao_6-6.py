# Exercício 6 - Seção 6.

# Programa onde uma sequência de três valores com casas decimais informados pelo usuário serão analisados e o valor de sua média será retornada.
# A quantidade de verificações a serem realizadas será definida pelo usuário.
# Para cada um dos três valores digitados será dado um peso diferenciado.
# Valor 1 peso 2 / Valor 2 peso 3 / Valor 3 peso 5.

# Mensagem de apresentação do programa.
print("Calculador de média")
print(" ")
print("Informe quantas verificações deseja realizar: ")
qtd_iteracoes = int(input(f"Digite um valor inteiro qualquer: "))

# Definição do loop for para as verificações.
for i in range(qtd_iteracoes):
    valor_x = float(input("Informe o primeiro valor: "))
    valor_y = float(input("Informe o segundo valor: "))
    valor_z = float(input("Informe o terceiro valor: "))
    media = (valor_x*2 + valor_y*3 + valor_z*5) / 10.0
    print(" ")
    print(f"Teste de número: {i+1}")
    print(f"Resultado: {media:.1f}")
    print("---------------------------------")

# Finalização do programa
print("Fim do programa")