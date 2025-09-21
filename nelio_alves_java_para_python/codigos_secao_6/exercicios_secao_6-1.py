# Exercício 1 - Seção 6.

# Programa verificador de senha fazendo uso do loop while.
# Senha correta 2002.

print("Programa que simula a tentativa de login em um sistema.")

# Definição das variáveis para a entrada dos dados.
nome = input("Digite seu nome de usuário: ")
senha = int(input("Informe sua senha: "))

# Criação de loop while para checagem da senha.
while (senha != 2002): # Enquanto a senha for diferente de 2002.
    senha = int(input("Senha incorreta, tente novamente: ")) # Mensagem de orientação ao usuário.

# Mensagem informando o login bem sucedido.
print(f"Bem vindo {nome}.")
print("Acesso permitido.")
