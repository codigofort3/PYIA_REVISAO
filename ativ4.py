# Faça um programa que peça para n pessoas a sua
# idade, ao final o programa devera verificar se a média
# de idade da turma varia entre 0 e 25, 26 e 60 e maior
# que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.

# Solicita a quantidade de pessoas

n = int(input("Digite o número de pessoas na turma: "))

idades = []

# Coleta a idade de cada pessoa
for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)
    
# Calcula a média das idades

media = sum(idades) / n

# Calcula a média das idades

if media <= 25 :
    print(f'Média de idade : {media:.2f} - Turma jovem.')
    
elif 26 <= media <= 60:
    print(f'Média de idade: {media:.2f} - Turma adulta')
    
else:
    print(f'Média de idade: {media:.2f} - Turma idosa.')
    
    
# O que esse código faz:
# Pede o número de pessoas.

# Coleta as idades uma por uma.

# Calcula a média.

# Classifica a turma como:

# Jovem se a média for até 25,

# Adulta se estiver entre 26 e 60,

# Idosa se for maior que 60.