# Peça a idade do usuário com base na idade fornecida, o programa deve
# classificar a pessoa em uma das seguintes categorias:
# Se a idade for menor que 12 anos, imprimir
# "Criança
# ".
# Se a idade estiver entre 12 e 17 anos (inclusive), imprimir
# "Adolescente
# ".
# Se a idade estiver entre 18 e 59 anos (inclusive), imprimir
# "Adulto
# ".
# Se a idade for igual ou superior a 60 anos, imprimir
# "Idoso
# ".

Idade = int(input("Quantos anos você tem?: "))
if Idade < 12:
    print(f"Você é  apenas uma crianç ,pois tem apenas {Idade} anos.")
    
elif Idade >= 12 and Idade <= 17:
    print(f"Você é um adolescente pois tem apenas {Idade} anos de idade.")
    
elif Idade >= 18 and Idade <= 59:
    print(f"Você já é um adulto, p59ois tem {Idade} anos de idade.")
    
else:
    print(f"Você já é idoso pois tem  {Idade} anos de idade. ")
    