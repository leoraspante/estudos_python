# Exercício 5 - Sessão 4.

# Mensagem de apresentação do programa.
print("Shopping Calculator.")
print(" ")

# Variáveis recebendo os valores de entrada do usuário, 1ª remessa.
cod_peca = int (input("Informe o código da peça escolhida: "))
qtd_pecas = int (input("Informe a quantidade de peças escolhidas: "))
valor_peca = float (input("Informe o valor da peça R$: "))

# Variáveis recebendo os valores de entrada do usuário, 2ª remessa.
cod_peca1 = int (input("Informe o código da peça escolhida: "))
qtd_pecas1 = int (input("Informe a quantidade de peças escolhidas: "))
valor_peca1 = float (input("Informe o valor da peça R$: "))

# Variável responsável pelo cálculo da 1ª remessa.
parcial_1 = qtd_pecas * valor_peca

# Variável responsável pelo cálculo da 2ª remessa.
parcial_2 = qtd_pecas1 * valor_peca1

# Variavel responsável pelo cálculo final da compra.
resultado = parcial_1 + parcial_2

# Exibição do resultado.
print(f"Código das peças escolhidas e quantidades: {cod_peca}, {qtd_pecas} unidades e {cod_peca1}, {qtd_pecas1} unidades.")
print(f"Valor total a pagar :R$ {resultado:.2f}.")
