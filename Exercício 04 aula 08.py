#Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda string lida está contida no
#final da primeira, imprimindo o resultado da verificação.
string1 = input('coloque uma string aqui! ')
string2 = input('coloque outra string aqui! ')
if string1.endswith(string2):
    print("Está no final")
else:
    print("Não está no final")