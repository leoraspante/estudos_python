# Programa que lê coordenadas X,Y no plano cartesiano.
# A execução é encerrada quando X ou Y for igual a zero.

# Mensagem de abertuda do programa.
print("Bem vindo ao QuadranteFinder.")
print("O programa será encerrado caso o valor de X ou Y seja igual a 0.")

# Definição das variáveis de entrada de dados.
valor_x = int(input("Informe o valor de X: "))
valor_y = int(input("Informe o valor de Y: "))

# Definição do loop while, onde temos a seguinte condição.
# Enquanto o valor de x e y forem diferentes de zero o loop continua sendo executado.
while (valor_x != 0 and valor_y != 0):

# Aplicações das condicionais if/else - Onde obtemos o posicionamento dos quadrantes.
	if (valor_x > 0 and valor_y > 0):
		print("Primeiro Quadrante.")
	elif (valor_x < 0 and valor_y > 0):
		print("Segundo Quadrante")
	elif (valor_x < 0 and valor_y < 0):
		print("Terceiro Quadrante")
	elif (valor_x > 0 and valor_y < 0):
		print("Quarto Quadrante")
	else:
		print("Valor inválido")
	
# Após a verificação do IF - O programa continua solicitando dados ao usuário.
# Uma vez que o bloco de código a seguir está identado dentro do loop while.
	valor_x = int(input("Informe o valor de X: "))
	valor_y = int(input("Informe o valor de Y: "))

# Fora do loop while, temos a mensagem de encerramento.
print("Fim do programa")
