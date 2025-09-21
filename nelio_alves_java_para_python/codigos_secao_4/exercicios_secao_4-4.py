# Exercício 4 - Seção 4.

# Mensagem de apresentação do programa.
print("Calculadora de salário.")
print(" ")

# Variáveis recebendo os valores de entrada do usuário.
cod_funcionario = int (input("Informe o código do funcionário: "))
horas_trabalhadas = float (input("Informe a quantidade de horas trabalhadas: "))
valor_hora = float (input("Informe o valor da hora R$: "))

# Variavel responsável pelo cálculo do salário.
resultado = horas_trabalhadas * valor_hora

# Exibição do resultado.
print(f"Código do funcionário = {cod_funcionario}.\nSalário a receber = U$ {resultado:.2f}.")
