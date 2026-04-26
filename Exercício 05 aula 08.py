#Escreva um programa que leia a idade e o primeiro nome de várias pessoas. Seu programa deve terminar quando uma
#idade negativa for digitada. Ao terminar, seu programa deve escrever o nome e a idade da pessoa mais jovem e mais velha.
nome = input('coloque o nome: ')
idade = int (input ('coloque a idade: '))
velha=nome
nova=nome
idade_velha = idade
idade_nova = idade
while idade>0:
    nome = input('coloque o nome: ')
    idade = int (input ('coloque a idade: '))
    if idade<0:
        break
    if idade>idade_velha:
        idade_velha=idade
        velha=nome
    if idade<idade_nova:
        idade_nova=idade
        nova=nome
print (f"\n A pessoa mais jovem é o/a {nova}, e a mais velha é o/a {velha}")