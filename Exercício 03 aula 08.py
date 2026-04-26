#Elabore um programa que leia nome, sexo e idade de um usuário. Se sexo for feminino e idade menor que 25,
#imprime o nome da pessoa e a palavra “ACEITA”, caso contrário imprimir “NÃO ACEITA”.
nome = input('Digite seu nome! ')
sexo = input('Digite seu sexo! ')
idade = int(input('Digite sua idade! '))
if sexo != "feminino" and sexo !="masculino":
    print ('Digite feminino ou masculino por favor')
    sexo = input('Digite seu sexo! ')
if sexo == "feminino":
    if idade < 25:
        print (f"\n {nome} ACEITO")
    else:
        print (f"\n {nome} NÃO ACEITO")
else:
    print (f"\n {nome} NÃO ACEITO")