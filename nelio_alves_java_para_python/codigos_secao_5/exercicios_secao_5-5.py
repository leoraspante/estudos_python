# Exercício 5 - Seção 5.

# Mensagem de apresentação do programa.
print("             CARDÁPIO              ")
print("CÓDIGO     ESPECIFICAÇÃO      PREÇO")
print("  1        Cachorro Quente   R$ 4.00")
print("  2        X-Salada          R$ 4.50")
print("  4        Torrada simples   R$ 2.00")
print("  5        Refrigerante      R$ 1.50")

# Variáveis recebendo os valores de entrada do usuário.
cod_produto = float (input("Informe o código do produto desejado: "))
qtd = float (input("Informe a quantidade desejada: "))

# Variáveis armazenando os valores dos produtos.
cod_1 = 4.00 # Preço cachorro quente.
cod_2 = 4.50 # Preço x-salada.
cod_3 = 5.00 # Preço x-bacon.
cod_4 = 2.00 # Preço torrada simples.
cod_5 = 1.50 # Preço refrigerante.


# Condicional responsável pela verificação do valor
if (cod_produto == 1): # Condição do cachorro quente.
    valor = qtd * cod_1
    print(f"Valor total: R$ {valor:.2f}")

elif (cod_produto == 2): # Condição x-salada.
    valor = qtd * cod_2
    print(f"Valor total: R$ {valor:.2f}")

elif (cod_produto == 3): # Condição x-bacon.
    valor = qtd * cod_3
    print(f"Valor total: R$ {valor:.2f}")

elif (cod_produto == 4): # Condição torrada simples.
    valor = qtd * cod_4
    print(f"Valor total: R$ {valor:.2f}")

else: # Condição refrigerante.
    valor = qtd * cod_5
    print(f"Valor total: R$ {valor:.2f}")

print(" ")
