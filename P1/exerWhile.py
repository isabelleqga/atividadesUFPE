# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("1. Somar os inteiros pares entre 50 e 100 (inclusive).")
soma1 = 0
i1 = 50
while i1 <= 100:
    soma1 += i1
    i1 += 2
print(f"A soma dos inteiros pares entre 50 e 100 é {soma1}.\n")

print("2. Calcular o fatorial de um número inteiro lido.")
fatorial2 = 1
i2 = 1
n2 = int(input("Digite um número inteiro:"))
while n2 < 0:
    print("Não há fatorial de um número negativo.")
    n2 = int(input("Digite um número válido:"))
while i2 != n2+1:
    fatorial2 *= i2
    i2 += 1
print(f"O fatorial de {n2} é {fatorial2}.\n")

print("3. Calcular o valor de S, onde S = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50")
soma3 = 0
numerador3 = 1
denominador3 = 1
while denominador3 != 51:
    soma3 += numerador3/denominador3
    numerador3 += 2
    denominador3 += 1
print(f"O valor de S é {round(soma3,2)}\n")

print("4. Calcular o valor de S com N termos, onde N é informado pelo usuário e S = 2/500 - 5/490 + 2/480 - 5/470...")
n4 = int(input("Digite um número de termos para a equação:"))
i4 = 1
soma4 = 0
denominador4 = 500
while n4 > 50 or n4 <= 0:
    print("Com esse número de termos o denominador da equação será zerado.")
    n4 = int(input("Digite um número de termos válido:"))
while i4 != n4:
    if i4 % 2 != 0:
        soma4 += 2/denominador4
        denominador4 -= 10
    else:
        soma4 -= 5/denominador4
        denominador4 -= 10
    i4 += 1
print(f"A soma da equação com {n4} termos é {round(soma4,2)}.\n")

print("5. Somar os inteiros ímpares entre dois valores inteiros informados pelo usuário.")
n5 = int(input("Digite um número inteiro:"))
n51 = int(input("Digite outro número inteiro:"))
soma5 = 0
if n51 < n5:
    n51, n5 = n5, n51
print(f"A soma dos inteiros ímpares entre {n5} e {n51} é ", end="")
if n5 % 2 == 0:
    n5 += 1
if n51 % 2 == 0:
    n51 -= 1
while n5 <= n51:
    soma5 += n5
    n5 += 2
print(f"{soma5}\n")

print("6. Construir uma tabela de conversão de graus Fahrenheit para Celsius em um intervalo informado pelo usuário.")
n6 = int(input("Digite um número inteiro:"))
n61 = int(input("Digite outro número inteiro:"))
if n61 < n6:
    n61, n6 = n6, n61
while n6 <= n61:
    c6 = ((n6-32)*5)/9
    print(f"| {n6}F | {round (c6, 1)}ºc |")
    n6 += 1
print("")

print("7. Ler um número inteiro N e imprimir o valor do n-ésimo termo da sequência [-1, 0, 5, 6, 11, 12, 17, 18, ...]")
n7 = int(input("Digite um número inteiro:"))
s7 = -1
cont7 = 1
while n7 <= 0:
    print("Impossível calcular uma posição menor ou igual a 0.")
    n7 = int(input("Digite um número válido:"))
while cont7 < n7:
    if cont7 % 2 != 0:
        s7 += 1
    else:
        s7 += 5
    cont7 += 1
print(f"O {n7}-ésimo termo da sequência é {round(s7,2)}\n")

print("8. Calcular o valor de S com N termos, onde N é informado pelo usuário e S = 37*38/1 + 36*37/2 + 35*36/3 + ...")
n8 = int(input("Digite um número inteiro:"))
s8 = 0
cont8 = 0
while n8 <= 0:
    print("Impossível calcular um número de termos menor ou igual a 0.")
    n8 = int(input("Digite um número válido:"))
while cont8 < n8:
    s8 += ((37 - cont8) * (38 - cont8)) / (cont8 + 1)
    cont8 += 1
print(f"O valor de S é {round(s8,2)}\n")

print("9. Calcular o menor de uma série de números inteiros lidos. A leitura dos números deve parar quando "
      "o número zero for lido.")
n9 = int(input("Digite um número inteiro:"))
while n9 == 0:
    n9 = int(input("O primeiro número não pode ser 0. Digite outro número inteiro:"))
menor9 = n9
while n9 != 0:
    if n9 <= menor9:
        menor9 = n9
    n9 = int(input("Digite um número inteiro:"))
print(f"O menor número digitado é {menor9}")

print("10. Calcular a média aritmética de vários números reais fornecidos pelo usuário. A leitura dos números "
      "deve parar quando um número negativo for lido.")
div10 = 0
soma10 = 0
n10 = float(input("Digite um número real:"))
while n10 < 0:
    n10 = float(input("O primeiro número não pode ser negativo. Digite um número real:"))
while n10 >= 0:
    soma10 += n10
    div10 += 1
    n10 = float(input("Digite um número real:"))
media10 = soma10/div10
print(f"A média aritmética dos números digitados é {media10}")

print("11. Ler um número inteiro e dizer se ele é primo ou não.")
n11 = int(input("Digite um número inteiro:"))
div11 = 2
ehprimo = True
while div11 <= 10:
    if n11 % div11 == 0 and n11 != div11:
        ehprimo = False
    div11 += 1
if ehprimo:
    print(f"O número {n11} é primo.")
else:
    print(f"O número {n11} não é primo.")

print("12. Ler um número inteiro e dizer se ele é perfeito ou não. Um número é perfeito se ele é igual "
      "à soma de todos os seus divisores (exceto ele mesmo")
n12 = int(input("Digite um número inteiro:"))
div12 = 1
soma12 = 0
while div12 < n12:
    if n12 % div12 == 0:
        soma12 += div12
    div12 += 1
if soma12 == n12:
    print(f"O número {n12} é perfeito.")
else:
    print(f"O número {n12} não é perfeito.")
