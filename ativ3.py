# Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a
# quantidade de números impares.

# Inicializa contadores de pares e ímpares


pares  = 0
impares = 0

# Loop para receber 10 números

for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    
 # Verifica se o número é par ou ímpar

    if num % 2 == 0:
        pares += 1
    
    else:
        impares += 1
    
# Exibe os resultados

print(f"Quantidade de números pares : {pares} ")
print(f"Quantidade de números impares : {impares} ")
    