#DESAFIO!!! Faça um programa que, dada uma string, diga se ela e um palíndromo ou não. Lembrando que um palíndromo e
#uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita.
palindromo = input('digite uma palavra: ')
palindromo = palindromo.lower()
palindromo = palindromo.replace(" ","")
invertida = palindromo [::-1]
if palindromo == invertida:
    print(f"\n Parabens {palindromo} é um palindromo")
else:
    print(f"\n ish {palindromo} não é um palindromo")