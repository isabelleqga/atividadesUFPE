# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("1. Somar os inteiros pares entre 50 e 100 (inclusive).")
soma1 = 0
for i1 in range(50, 101, 2):
    soma1 += i1
print(f"A soma dos inteiros pares entre 50 e 100 é {soma1}\n")

print("2. Calcular o fatorial de um número inteiro lido.")
numero2 = int(input("Digite um número inteiro:"))
fatorial2 = 1
if numero2 < 0:
    print("Não há fatorial de um número negativo.\n")
else:
    for i2 in range(1, numero2+1):
        fatorial2 *= i2
    print(f"O fatorial de {numero2} é {fatorial2}\n")

print("3. Calcular o valor de S, onde S = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50")
numerador3 = 1
denominador3 = 1
s3 = 0
for denominador3 in range(1, 51):
    s3 += numerador3/denominador3
    numerador3 += 2
print(f"O valor de S é {round(s3,2)}\n")

print("4. Calcular o valor de S com N termos, onde N é informado pelo usuário e S = 2/500 - 5/490 + 2/480 - 5/470 + ...")
n4 = int(input("Digite um número inteiro:"))
s4 = 0
denominador4 = 500
if n4 <= 0:
    print("Impossível calcular com um número de termos menor ou igual a zero.\n")
elif n4 > 50:
    print("Erro: Divisão por zero.\n")
else:
    for i4 in range(1, n4+1):
        if i4 % 2 != 0:
            s4 += 2/denominador4
            denominador4 -= 10
        else:
            s4 -= 5/denominador4
            denominador4 -= 10
    print(f"O valor de S com {n4} termos é {round(s4,2)}\n")

print("5. Somar os inteiros ímpares entre dois valores inteiros informados pelo usuário.")
n5 = int(input("Digite um número inteiro:"))
n51 = int(input("Digite outro número inteiro:"))
soma5 = 0
if n51 < n5:
    n51, n5 = n5, n51
for i5 in range(n5, n51+1):
    if i5 % 2 != 0:
        soma5 += i5
print(f"A soma dos inteiros ímpares entre {n5} e {n51} é {soma5}\n")

print("6. Construir uma tabela de conversão de graus Fahrenheit para Celsius em um intervalo informado")
n6 = int(input("Digite um número inteiro:"))
n61 = int(input("Digite outro número inteiro:"))
if n61 < n6:
    n61, n6 = n6, n61
for f6 in range(n6, n61+1):
    c6 = ((f6-32)*5)/9
    print(f"| {f6}F | {round (c6, 1)}ºc |")
print("")

print("7. Ler um número inteiro N e imprimir o valor do n-ésimo termo da sequência [-1, 0, 5, 6, 11, 12, 17, 18, ...]")
n7 = int(input("Digite um número inteiro:"))
sequencia7 = -1
if n7 <= 0:
    print("Impossível calcular uma posição menor ou igual a 0.\n")
else:
    for i7 in range(1, n7):
        if i7 % 2 != 0:
            sequencia7 += 1
        else:
            sequencia7 += 5
    print(f"O {n7}-ésimo termo da sequência é {round(sequencia7,2)}\n")

print("8. Calcular o valor de S com N termos, onde N é informado pelo usuário e S = 37*38/1 + 36*37/2 + 35*36/3 + ...")
n8 = int(input("Digite um número inteiro:"))
s8 = 0
if n8 <= 0:
    print("Impossível calcular um número de termos menor ou igual a 0.\n")
else:
    for i8 in range(0, n8):
        s8 += ((37-i8)*(38-i8))/(i8+1)
    print(f"O valor de S é {round(s8,2)}\n")

print("9. Dado número inteiro, imprima a tabuda de multiplicação até ele mesmo, sem usar o operador de multiplicação.")
n9 = int(input("Digite um número inteiro:"))
if n9 < 0:
    print("Operação inválida para essa questão.")
else:
    for i9 in range(0, n9+1):
        soma9 = 0
        for j9 in range(0, i9):
            soma9 += n9
        print(f"| {n9} x {i9} = {soma9} |")

