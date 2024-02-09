print("1. Faça um programa que receba dois números inteiros de entrada, e calcule a soma dos números primos "
      "entres esses dois números (intervalo fechado).")

n1 = int(input("Digite um número inteiro:"))
n11 = int(input("Digite outro número inteiro:"))
div1 = 2
soma1 = 0
ehprimo = True
for i1 in range(n1, n11+1):
      while div1 <= 10 and ehprimo:
            if i1 % div1 == 0 and i1 != div1:
                  ehprimo = False
            div1 += 1
      if ehprimo:
            soma1 += i1
      div1 = 2
      ehprimo = True
print(f"A soma dos números primos entre {n1} e {n11} é {soma1}.\n")


print("#2. Faça um programa que receba uma certa quantidade de números positivos de entrada e determine qual o "
      "maior e o menor valor entre os números selecionados. O programa deverá finalizar quando a entrada for "
      "negativa (esse não deve entrar pra contagem).")
n2 = int(input("Digite um número inteiro:"))
while n2 < 0:
    n2 = int(input("O primeiro número não pode ser negativo. Digite outro número inteiro:"))
menor2, maior2 = n2, n2
while n2 > 0:
      if n2 <= menor2:
            menor2 = n2
      if n2 >= maior2:
            maior2 = n2
      n2 = int(input("Digite um número inteiro:"))
print(f"O maior número digitado é {maior2}.")
print(f"O menor número digitado é {menor2}.\n")

print("3. Faça um programa que receba uma certa quantidade de números positivos de entrada, até que a soma "
      "desses números ultrapasse 1000. Depois determine qual a média dos números passados.")
n3 = int(input("Digite um número positivo:"))
soma3 = 0
cont3 = 0
while soma3 <= 1000:
      if n3 < 0:
            n3 = int(input("O número não pode ser negativo. Digite um número positivo:"))
      else:
            soma3 += n3
            cont3 += 1
      if soma3 <= 1000:
            n3 = int(input("Digite um número positivo:"))
media3 = soma3/cont3
print(f"A média dos números é {media3}.\n")

print("4. Faça um programa que receba um número inteiro e calcule a sequência de Fibonacci até esse termo.")
n5 = int(input("Digite um número de termos para a sequência Fibonacci:"))
fibo5 = 1
fibo15 = 0
fibo25 = 0
while n5 <= 0:
      n5 = int(input("Quantidade inválida. Digite um número de termos para a sequência Fibonacci:"))
print("0", end=" ")
while n5 != 0:
      print(fibo5, end=" ")
      fibo15, fibo25 = fibo5, fibo15
      fibo5 = fibo15 + fibo25
      n5 -= 1
