# Exercício 8 - Sessão 5.

# Mensagem de apresentação do programa.
print("Cálculo de imposto de renda")
print(" ")

# Mensagem personalizado com os valores referenciais.
print("Renda Salarial               Imposto de Renda");
print("     Faixa                       Tributação");
print("De R$ 0.00 até R$ 2000.00          Isento");
print("De R$ 2000.01 até R$ 3000.00         8%");
print("De R$ 3000.01 até R$ 4500.00         18%");
print("Acima de R$ 4500.00                  28%");

# Variáveis recebendo os valores de entrada do usuário.
salario = float (input("Informe o valor de X: "))
print(" ")

# Condicionais de verificação
if (salario < 2000.00): # Isento de impostos.
    print("Isento de impostos.")

elif (salario <= 3000.00): # Faixa de 8%.
    imposto = (salario - 2000.00) * 0.08
    print(f"Total a contribuir: R$ {imposto:.2f}.")

elif (salario <= 4500.00): # Faixa de 18%.
    imposto = (1000.00 * 0.08) + (salario - 3000.00) * 0.18
    print(f"Total a contribuir: R$ {imposto:.2f}.")

else : # Faixa de 28%.
    imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + (salario - 4500.00) * 0.28
    print(f"Total a contribuir: R$ {imposto:.2f}.")

