# Você foi contratado para desenvolver um programa simples para
# auxiliar em um processo de compra de produtos. O programa deve
# permitir ao usuário inserir o nome e o preço de vários produtos,
# perguntando se deseja continuar inserindo mais produtos após cada
# entrada. Ao final, o programa deve fornecer um resumo da compra,

# incluindo:

# A) O total gasto na compra.

# B) A quantidade de produtos que custam mais de R$1000.

# C) O nome do produto mais barato.
# Desenvolva o programa em Python utilizando conceitos de
# entrada/saída de dados, condicionais e laços de repetição.

total = 0
mais_de_1000 = 0
produto_mais_barato = ''
preco_mais_barato = None

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Digite o preço do produto (R$): "))
    
    #Soma total
    total += preco
    
      # Conta os produtos acima de R$1000
      
    if preco > 1000:
        mais_de_1000 += 1
        
     # Verifica o produto mais barato
     
    if preco_mais_barato  is None or preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome
        
     # Pergunta se o usuário quer continuar
    continuar = input("Deseja adicionar mais produtos? [S/N]: ").strip().upper()
    if continuar !=  "S" :
        break
    
# Exibe o resumo da compra
print("\n======RESUMO DA COMPRA=====")
print(f"Total de gastos : R${total:.2f}")
print(f"produtos com preço acima de R$ 1000: {mais_de_1000}")
print(f"Produtos mais baratos: {produto_mais_barato} (R${preco_mais_barato:.2f})")



# total = 0
# mais_de_1000 = 0
# produto_mais_barato = ''
# preco_mais_barato = None
# Explicação:

# total = 0: variável que vai acumular o valor total gasto na compra.

# mais_de_1000 = 0: contador para saber quantos produtos custam mais de R$1000.

# produto_mais_barato = '': variável que vai armazenar o nome do produto mais barato.

# preco_mais_barato = None: armazena o preço do produto mais barato. Começa com None porque ainda não foi definido.


# while True:
# while True:: inicia um laço infinito. Ele só vai parar quando o usuário disser que não quer continuar.


#     nome = input("Nome do produto: ")
# Pede ao usuário que digite o nome do produto.


#     preco = float(input("Preço do produto (R$): "))
# Pede o preço do produto, convertendo para float (número com casas decimais).


#     total += preco
# Soma o preço do produto ao total gasto até agora.


#     if preco > 1000:
#         mais_de_1000 += 1
# Se o produto custa mais de R$1000, incrementa o contador mais_de_1000.


#     if preco_mais_barato is None or preco < preco_mais_barato:
#         preco_mais_barato = preco
#         produto_mais_barato = nome
# Essa parte verifica se o produto atual é o mais barato até agora.

# Se preco_mais_barato ainda for None (ou seja, nenhum produto ainda foi avaliado), ou se o preço atual for menor que o menor preço anterior, atualiza preco_mais_barato e produto_mais_barato.


#     continuar = input("Deseja adicionar mais produtos? [S/N]: ").strip().upper()
# Pergunta ao usuário se ele quer continuar.

# O .strip() remove espaços extras e o .upper() transforma a letra digitada em maiúscula.


#     if continuar != 'S':
#         break
# Se o usuário digitar qualquer coisa diferente de 'S', o laço é interrompido com break.


# print("\n===== RESUMO DA COMPRA =====")
# print(f"Total gasto: R${total:.2f}")
# print(f"Produtos com preço acima de R$1000: {mais_de_1000}")
# print(f"Produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})")


# Explicação final:
# Imprime o resumo da compra:

# total: mostra o valor total formatado com 2 casas decimais.

# mais_de_1000: mostra quantos produtos passaram de R$1000.

# produto_mais_barato: mostra o nome e o preço do produto mais barato, também formatado com 2 casas decimais.