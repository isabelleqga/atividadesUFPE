print("1. Ler 2 vetores de tamanho N, com N informado pelo usuário antes, somar os 2 vetores, "
      "imprimir os 2 vetores e depois o vetor resultado.")
tamanho1 = int(input("Digite o tamanho das listas:"))
lista1 = []
lista11 = []
for i1 in range(tamanho1):
    lista1.append(int(input("Digite um elemento da primeira lista:")))
for i1 in range(tamanho1):
    lista11.append(int(input("Digite um elemento da segunda lista:")))
# Concatenando:
listaf1 = lista1 + lista11
print(f"Duas listas concatenadas: {listaf1}")
# Somando os valores:
listaf11 = lista1
for i1 in range(tamanho1):
    listaf11[i1] = lista1[i1] + lista11[i1]
print(f"Valores somados: {listaf11}\n")


print("2. Ler uma lista de N números (N é informado pelo usuário antes), e depois criar duas outras listas "
      "com os números pares e ímpares separados. No final imprimir as 3 listas.")
tamanho2 = int(input("Digite o tamanho da lista:"))
lista2 = []
lista2par = []
lista2impar = []
for i2 in range(tamanho2):
    lista2.append(int(input("Digite um elemento da lista:")))
for elemento2 in lista2:
    if elemento2 % 2 == 0:
        lista2par.append(elemento2)
    if elemento2 % 2 != 0:
        lista2impar.append(elemento2)
print(f"Lista original: {lista2}")
print(f"Pares: {lista2par}")
print(f"Ímpares: {lista2impar}\n")


print("3. Ler as notas de N alunos (N é informado pelo usuário antes), calcular e imprimir a média das "
      "notas e depois imprimir as notas que sejam maiores do que a média calculada.")
tamanho3 = int(input("Digite a quantidade de alunos:"))
tamanho33 = int(input("Digite a quantidade de notas:"))
alunos3 = []
soma3 = 0
for i3 in range(tamanho3):
    alunos3.append([0]*tamanho33)
for i3 in range(tamanho3):
    for j3 in range(tamanho33):
        alunos3[i3][j3] = int(input(f"Digite uma nota do aluno {i3}:"))
print("\n")
for i3 in range(tamanho3):
    for j3 in range(tamanho33):
        soma3 += alunos3[i3][j3]
    media3 = soma3/tamanho33
    print(f"Aluno número {i3}")
    print(f"Notas: {alunos3[i3]}")
    print(f"Média: {media3}")
    print(f"Notas acima da média:", end=' ')
    for j3 in range(tamanho33):
        if alunos3[i3][j3] > media3:
            print(alunos3[i3][j3], end=' ')
    soma3 = 0
    print("\n")


print("4. Fazer um programa Python para: "
      "– Ler uma sequência de números inteiros positivos (ou zero). "
      "– A leitura deve parar com um número negativo. "
      "– O programa deve imprimir os números lidos cujos valores têm dois dígitos, mas na "
      "ordem inversa em que forem lidos – o último número lido deve ser o primeiro a ser impresso.")
lista4 = []
listafinal4 = []
elemento4 = int(input("Digite um elemento da lista:"))
lista4.append(elemento4)
while elemento4 < 0:
    print("O primeiro número não pode ser negativo.")
    lista4.pop()
    elemento4 = int(input("Digite um elemento da lista:"))
    lista4.append(elemento4)
while elemento4 >= 0:
    elemento4 = int(input("Digite um elemento da lista:"))
    lista4.append(elemento4)
lista4.pop(-1)
for elemento4 in lista4:
    if elemento4 > 9 and elemento4 < 100:
        listafinal4.append(elemento4)
print(f"Lista original: {lista4}")
print(f"Lista final: {listafinal4}")
print(f"Lista final reversa: {list(reversed(listafinal4))}")

print("5. Altere o programa anterior para garantir que o usuário digitará no máximo 1000 números.")
lista5 = []
listafinal5 = []
elemento5 = int(input("Digite um elemento da lista:"))
lista5.append(elemento5)
cont = 1
while elemento5 < 0:
    print("O primeiro número não pode ser negativo.")
    lista5.pop()
    elemento5 = int(input("Digite um elemento da lista:"))
    lista5.append(elemento5)
while (cont < 1000) and (elemento5 >= 0):
    elemento5 = int(input("Digite um elemento da lista:"))
    lista5.append(elemento5)
    cont += 1
if elemento5 < 0:
    lista5.pop(-1)
for elemento5 in lista5:
    if (elemento5 > 9) and (elemento5 < 100):
        listafinal5.append(elemento5)
print(f"Lista original: {lista5}")
print(f"Lista final: {listafinal5}")
print(f"Lista final reversa: {list(reversed(listafinal5))}")