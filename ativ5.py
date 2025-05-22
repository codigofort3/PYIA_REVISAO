# Faça um programa que, dado um conjunto de N
# números, determine o menor valor, o maior valor e a

# soma dos valores.

# Solicita a quantidade de números
n = int(input("Quantos números você quer iserir? :"))

numeros = []

# Coleta os números
for i in range(n):
    numero = float(input(f"Digite o número {i+1}º número: "))
    numeros.append(numero)
    
# Calcula menor, maior e soma

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

# Exibe os resultados
print(f"\nMenor valor : {menor}")
print(f"Maior valor : {maior}")
print(f"Soma dos valores : {soma}")
