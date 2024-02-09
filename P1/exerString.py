print("1. Ler o nome do usuário e imprimi-lo na vertical, ou seja, uma letra embaixo da outra.")
nome1 = input("Digite o seu nome:")
for s1 in nome1:
    print(f"{s1}")

print("2. Ler o nome do usuário e imprimi-lo em formato de escala, ou seja, só a primeira letra "
      "na primeira linha, as duas primeiras letras na segunda linha, e assim por diante.")
nome2 = input("Digite uma palavra:")
a2 = 0
b2 = 1
cont2 = 1
for s2 in nome2:
    print(nome2[a2:b2])
    cont2 += 1
    a2 = b2
    b2 += cont2

print("3. Ler 2 strings e dizer quantas vezes o primeiro aparece no segundo.")
nome3 = input("Digite uma palavra:")
nome33 = input("Digite outra palavra:")
resultado3 = nome33.find(nome3)
cont3 = 0
while resultado3 != -1:
    cont3 += 1
    resultado3 = nome33.find(nome3, resultado3+1)
if resultado3 == -1:
    resultado3 = 0
print(f"A palavra {nome3} aparece {cont3} vez(es) em {nome33}")
# BOY KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
# Jeito FÁCIL:
print("3. Ler 2 strings e dizer quantas vezes o primeiro aparece no segundo.")
nome3 = input("Digite uma palavra:")
nome33 = input("Digite outra palavra:")
resultado3 = nome33.count(nome3)
print(f"A palavra {nome3} aparece {resultado3} vez(es) em {nome33}")

print("4. Ler o nome completo do usuário e imprimi-lo com o primeiro e último nome escritos todo em maiúsculas.")
nome4 = input("Digite seu nome completo:")
nome4 = nome4.strip()
pposi4 = nome4.find(' ')
uposi4 = nome4.rfind(' ')
primeiro4 = nome4[:pposi4].upper()
ultimo4 = nome4[uposi4:].upper()
nomefinal4 = nome4.replace(nome4[:pposi4], primeiro4)
nomefinal4 = nomefinal4.replace(nome4[uposi4:], ultimo4)
print(nomefinal4)