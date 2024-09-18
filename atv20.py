# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.
soma_pares = 0

# Loop para percorrer os números de 1 a 100
for numero in range(1, 101):
    if numero % 2 == 0:  # Verifica se o número é par
        soma_pares += numero  # Adiciona o número par à soma

# Exibe o resultado
print(f"A soma dos números pares de 1 a 100 é {soma_pares}.")