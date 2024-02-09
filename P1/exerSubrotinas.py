# Fazer um programa para:
# – Ler números inteiros positivos de até 5 dígitos (consistir) e imprimir quantas vezes o dígito 9 ocorre em cada um.
# – A leitura pára com número negativo ou zero.
# – Escrever subrotina que deve desmembrar o valor do número em seus 5 dígitos, retornando o resultado em uma lista de tamanho 5.

# – Escrever outra subrotina que usa a anterior e que:
# • Recebe como parâmetros um número positivo até 99999 e um algarismo inteiro (0 a 9), nesta ordem.
# • Retorne como resultado a quantidade vezes que o algarismo aparece no número.

print("\nQuestão 1")
def desmembrando(num):
    string = str(num)
    numeroDesmembrado = [0] * 5
    for i in range(len(string)):
        numeroDesmembrado[i] = string[i]
    return numeroDesmembrado

def contandoVezes(numero, algarismo=9):
    numero = desmembrando(numero)
    algarismoString = str(algarismo)
    contagem = 0
    for n in numero:
        if algarismoString == n:
            contagem += 1
    return contagem

numero = int(input("Digite um número inteiro positivo de até 5 dígitos: "))
while (numero <= 0) or (numero > 99999):
    numero = int(input("Número inválido. Digite um número inteiro positivo de até 5 dígitos: "))
while numero > 0:
    contagem = contandoVezes(numero)
    print(f"O algarismo 9 aparece {contagem} vezes no número {numero}.")
    print("\n::::::::::Nova leitura::::::::::")
    numero = int(input("Digite um número inteiro positivo de até 5 dígitos: "))
    while numero > 99999:
        numero = int(input("Digite um número inteiro positivo de até 5 dígitos: "))

print("\n::::::::::Nova rotina::::::::::")
numero = int(input("Digite um número inteiro positivo de até 5 dígitos: "))
while (numero <= 0) or (numero > 99999):
    numero = int(input("Número inválido. Digite um número inteiro positivo de até 5 dígitos: "))
algarismo = int(input("Digite um número entre 0 e 9: "))
while (algarismo < 0) or (algarismo > 9):
    algarismo = int(input("Número inválido. Digite um número entre 0 e 9: "))
contagem = contandoVezes(numero, algarismo)
print(f"O algarismo {algarismo} aparece {contagem} vezes no número {numero}.")

# Fazer um programa para achar todos os números palíndromos entre 100 e 5000.
# – Um número é palíndromo se ele tiver o mesmo valor quando escrito da direita para a esquerda. Ex: 17371.
# – Escreva e utilize uma subrotina cujo resultado é o valor recebido no parâmetro (int) escrito ao contrário.
# • Pode ser interessante utilizar a subrotina da questão anterior para desmembramento dos números.
print("\nQuestão 2")

# – Escreva e utilize uma subrotina cujo resultado é o valor recebido no parâmetro (int) escrito ao contrário.
def aoContrario(numero):
    numeroSTR = str(numero)
    numeroOposto = ''
    for i in range(len(numeroSTR)):
        numeroOposto = numeroSTR[i] + numeroOposto
    return numeroOposto

for i in range (100, 5001):
    numeroOposto = aoContrario(i)
    if numeroOposto == str(i):
        print(i)

#1. Faça um programa que recebe do usuário uma lista de inteiros com tamanho N (também defindo pelo usuário).
# Em seguida, escreva uma função que recebe essa lista como parâmetro e retorna uma outra lista (possivelmente menor)
# sem conter elementos repetidos.

def semRepeticao (lista):
    lista2 = [0]* len(lista)
    contador = 0
    for i in range (len(lista)):
        tem = False
        for j in range (len(lista2)):
            if lista[i] == lista2[j]:
                tem = True
        if not tem:
            lista2[i] = (lista[i])
            contador += 1
    lista2 = lista2[0:contador]
    return lista2

n = int(input("Digite o tamanho da lista: "))
lista = [0]*n
for i in range(n):
    lista[i] =  int(input("Digite um elemento da lista: "))
lista2 = semRepeticao(lista)
print(lista)
print(lista2)