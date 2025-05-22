# Faça um programa que leia 3 números e informe o
# maior número e o menor.

# Solicita três números ao usuário

# - Aqui, o programa pede ao usuário para digitar um número.
# - input("Digite o primeiro número: ") exibe a mensagem e aguarda a entrada do usuário.
# - float() converte essa entrada (que vem como texto) para um número decimal (ponto flutuante).



num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

#Determina o maior e o menos número

#- A função max() recebe os três números e retorna o maior deles.
#- O valor retornado é armazenado na variável maior.
maior = max(num1, num2, num3)

#- Aqui, a função min() faz o oposto: retorna o menor número dos três e armazena em menor.

menor = min(num1, num2, num3)

# Exibe os resultados

#- O comando print() exibe as mensagens no console.
#O uso de f"" (f-string) permite incluir diretamente o valor das variáveis maior e menor dentro do tex

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")