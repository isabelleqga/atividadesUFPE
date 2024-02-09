n = int(input("Digite o número de termos da expressão: "))
while n <= 0:
    n = int(input("O número deve ser positivo. Digite o número de termos da expressão: "))
s = 0
numeradorImpar = 100
numeradorPar = 13
denominador = 1
for i in range(1, n+1):
    if i % 2 != 0:
        s += numeradorImpar/denominador
        numeradorImpar -= 5
    else:
        s -= numeradorPar/denominador
        numeradorPar += 11
    denominador *= i+1
print(f"O valor com {n} termos é de {s}")

print("O Mínimo Múltiplo Comum (MMC) de 2 números inteiros positivos é definido como o "
       "menor número inteiro positivo que é múltiplo de ambos. Faça um programa Python para ler 2"
       "números inteiros positivos no início e procurar/descobrir o MMC destes 2 números. ")
n1 = int(input("Digite um número positivo: "))
while n1 <= 0:
      n1 = int(input("Número deve ser positivo. Digite um número positivo: "))
n2 = int(input("Digite outro número positivo: "))
while n2 <= 0:
      n2 = int(input("Número deve ser positivo. Digite um número positivo: "))
mmc = 0
contador = 1
while mmc == 0:
    if (contador % n1 == 0) and (contador % n2 == 0):
        mmc = contador
    contador += 1
print(f"O mmc de {n1} e {n2} é {mmc}")

print("Faça um programa Python para ler uma tabela de pessoas onde:"
      "• Cada pessoa tem um cpf (long), um nome (String) e um salário (float)."
      "• A leitura da tabela pára com um cpf que não seja positivo."
      "• O usuário só pode digitar no máximo 300 pessoas."
      "Depois o usuário informará um intervalo de salários (fechado), ou seja, os limites inferior e"
      "superior do intervalo. Ambos devem ser positivos, mas o limite inferior pode ser zero. Além"
      "disto, o limite inferior do intervalo deve ser menor do que o limite superior. Caso alguma"
      "restrição seja violada, o programa deve informar ao usuário e pedir os dados novamentre."
      "De posse de um intervalo correto, o seu programa deve imprimir os dados das pessoas que se"
      "enquadram no intervalo, seguidos pelo número de pessoas do intervalo, pelo maior salário e"
      "pela média dos salários destas pessoas. O seu programa deve informar ainda quantas pessoas"
      "têm salários maiores do que o limite superior do intervalo. ")
cpf = int(input("Digite o CPF da pessoa: "))
cont = 1
pessoas = {}
while cont < 301 and cpf > 0:
    nome = input("Digite o nome da pessoa: ")
    salario = float(input("Digite o salario da pessoa: "))
    pessoa = (cpf, nome, salario)
    pessoas[cont] = pessoa

    cpf = int(input("Digite o CPF da pessoa: "))
    cont += 1
print("\nFim da leitura de pessoas.\n")
salarioInicio = float(input("Digite o início do intervalo de salarios: "))
while salarioInicio < 0:
    print("Número inválido.")
    salarioInicio = float(input("Digite o início do intervalo de salarios: "))
salarioFinal = float(input("Digite o fim do intervalo de salarios: "))
while (salarioInicio < 0) or (salarioFinal < salarioInicio):
    print("Número inválido.")
    salarioFinal = float(input("Digite o fim do intervalo de salarios: "))
print("\nFim da leitura do intervalo.\n")
print("As pessoas que se enquadram nesse intervalo de salário são:")
contando = 0
contandoSobras = 0
soma = 0
for chave in pessoas:
    pessoaCPF, pessoaNome, pessoaSalario = pessoas[chave]
    if (pessoaSalario >= salarioInicio) and (pessoaSalario <= salarioFinal):
        print(f"- {pessoaCPF}, {pessoaNome}, {pessoaSalario}")
        if contando == 0:
            maiorSalario = pessoaSalario
        else:
            if maiorSalario < pessoaSalario:
                maiorSalario = pessoaSalario
        contando += 1
        soma += pessoaSalario
    else:
        contandoSobras += 1
print(f"\nO maior salário do intervalo é de {maiorSalario}")
print(f"A média de salários é de {soma/contando}")
print(f"A quantidade de pessoa fora do intervalo é de {contandoSobras}")

print("Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo, onde o valor "
    "de N deve ser informado pelo usuário no início. O seu programa deve imprimir o resultado (com 4 "
    "casas decimais) da seguinte forma: “O valor da série com ... termos é ...”. "
    "S = 19 / 1 – 70 / 5 + 25 / 2 – 85 / 12 + 31 / 4 – 100 / 19 + 37 / 8 ...")
n = int(input("Digite um número inteiro:"))
s = 0
numeradorImpar = 19
denominadorImpar = 1
numeradorPar = 70
denominadorPar = 5
if n <= 0:
    print("Impossível calcular com um número de termos menor ou igual a zero.\n")
else:
     for i in range(1, n+1):
         if i % 2 != 0:
             s += numeradorImpar/denominadorImpar
             numeradorImpar += 6
             denominadorImpar *= 2
         else:
             s -= numeradorPar/denominadorPar
             numeradorPar += 15
             denominadorPar += 7
     print(f"O valor da série com {n} termos é {round(s,4)}\n")


print("Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo, onde "
      "o valor de N deve ser informado pelo usuário no início. O seu programa deve imprimir o "
      "resultado (com 4 casas decimais) da seguinte forma: “O valor da série com ... termos é ...”. "
      "S = 2 – 7 / 5 + 8 / 3 – 13 / 9 + 32 / 9 – 19 / 13 + 128 / 27 ...")
n = int(input("Digite um número inteiro:"))
while n <= 0:
    print("ERRO: Digite um número de termos positivo.")
    n = int(input("Digite um número inteiro:"))
s = 0
numeradorImpar = 2
denominadorImpar = 1
numeradorPar = 7
denominadorPar = 5
for i in range(1, n + 1):
    if i % 2 != 0:
        print(f" + {numeradorImpar}/{denominadorImpar}", end="")
        s += numeradorImpar / denominadorImpar
        numeradorImpar *= 4
        denominadorImpar *= 3
    else:
        print(f" - {numeradorPar}/{denominadorPar}", end="")
        s -= numeradorPar / denominadorPar
        numeradorPar += 6
        denominadorPar += 4
print(f"\nO valor da série com {n} termos é {round(s, 4)}\n")

print("Faça um programa Python para ler uma seqüência de números inteiros negativos – a leitura "
      "pára quando o número zero for lido. No entanto, o usuário só deve poder digitar no máximo"
      "150 números negativos. O programa deve imprimir as seguintes informações como resultado (nesta ordem):"
      " Os números lidos cujos valores têm 2 dígitos significativos e também são múltiplos de 5."
      "A impressão destes números deve ser feita na ordem inversa da que foram lidos."
      " O maior número lido que não seja múltiplo de 7.")
lista = []
elemento = int(input("Digite um elemento inteiro negativo:"))
while elemento >= 0:
    print("O primeiro número não pode ser positivo ou 0.")
    elemento = int(input("Digite um elemento inteiro negativo:"))
lista.append(elemento)
contagem = 1
paragem = True
while paragem and (contagem < 150):
    elemento = int(input("Digite um elemento inteiro negativo:"))
    if elemento > 0:
        print("O número não pode ser positivo.")
    elif elemento == 0:
        paragem = False
    else:
        lista.append(elemento)
        contagem += 1
listafinal1 = []
print("Número lidos cujos valores têm dois dígitos significativos e são múltiplos de 5: ", end="")
for elemento in lista:
    if ((elemento < -9) and (elemento > -100)) and (elemento % 5 == 0):
        listafinal1.append(elemento)
print(list(reversed(listafinal1)))
multiplos = []
haMultiplo7 = False
for elemento in lista:
    if elemento % 7 != 0:
        multiplos.append(elemento)
        haMultiplo7 = True
if haMultiplo7:
    maior = multiplos[0]
    for elemento in multiplos:
        if maior < elemento:
            maior = elemento
    print("O maior número que não é múltiplo de 7 é",maior)
else:
    print("Não há números que não sejam múltiplos de 7.")

print("– Faça um programa Python para ler e armazenar uma tabela de disciplinas onde:"
      " Cada disciplina tem um código (string com exatamente 5 caracteres), seu nome (string),"
      "sua carga horária (int, positivo) e seu número de créditos (int, positivo)."
      " A leitura da tabela pára com a digitação de ‘FIM’, ao invés de um código válido."
      " O usuário só pode digitar no máximo 500 disciplinas."
      "Depois o usuário informará um prefixo de código (string com menos de 5 caracteres) e o"
      "programa deve imprimir os dados das disciplinas cujos códigos começam pelo prefixo"
      "informado, bem como a média das cargas horárias dessas disciplinas. ")

disciplinas = {}
discCod = input('Digite o código da disciplina: ')
discCod.strip()
while len(discCod) != 5:
    discCod = input('Digite um código válido (5 caracteres): ')
    discCod.strip()
contagem = 0
while discCod != 'FIM' and (len(discCod) == 5 and contagem < 500):
    contagem += 1
    discNome = input(f'Digite o nome da disciplina {discCod}:')
    discCarga = int(input(f'Digite a carga horária da disciplina {discCod}: '))
    while discCarga <= 0:
        discCarga = int(input(f'Digite uma carga horária válida para a {discCod}: '))
    discCredito = int(input(f'Digite os créditos da disciplina {discCod}: '))
    while discCredito <= 0:
        discCredito = int(input(f'Digite créditos válidos para a {discCod}: '))
    disciplinas[discCod] = (discNome, discCarga, discCredito)  # Inserção no dicionário...

    if contagem == 500:
        print("Limite de disciplinas atingidos.\n")
    else:
        print("\nDigite FIM para parar a leitura.")
        discCod = input('Digite o código da disciplina: ')
        while len(discCod) != 5 and discCod != 'FIM':
            discCod = input('Digite um código válido (5 caracteres): ')
            discCod.strip()
buscaCod = input('\nDigite um prefixo de código (<5 caracteres): ')
soma = 0
cont = 0
while len(buscaCod) >= 5:
    buscaCod = input('Digite um prefixo de código (<5 caracteres: ')
print("As disciplinas encontradas para a busca", buscaCod, "são:")
for codigo in disciplinas:
    if codigo[0:len(buscaCod)] == buscaCod:
        discNome, discCarga, discCredito = disciplinas[codigo]
        soma += discCarga
        cont += 1
        print(f"- {codigo}, {discNome}, {discCarga}, {discCredito}")
if cont == 0:
    print("A média de carga horária dessas disciplinas é de 0 horas.")
else:
    print(f"\nA média de carga horária dessas disciplinas é de {soma/cont} horas.")


print("Fazer um programa para:"
      "– Ler uma tabela de pessoas onde:"
      "• Cada pessoa tem código (int), nome (Str) e salário (float)."
      "• A leitura da tabela pára com um código <= 0."
      "– Depois o usuário informará um valor máximo de salário."
      "Caso o valor não seja positivo, o programa deve"
      "apontar o erro e pedir os dados novamente."
      "– O programa deve imprimir os dados das pessoas cujos"
      "salários sejam menores que o valor máximo informado,"
      "seguidos pelo número de pessoas correspondentes, e"
      "pela média dos salários destas pessoas.")

pessoas = {}
pessoaCod = int(input('Digite o código da pessoa: '))
while pessoaCod <= 0:
    pessoaCod = int(input('O primeiro código não pode ser menor que 1. Digite o código da pessoa: '))
while pessoaCod > 0:
    pessoaNome = input(f'Digite o nome da pessoa {pessoaCod}: ')
    pessoaSalario = float(input(f'Digite o salário da pessoa {pessoaCod}: '))
    pessoas[pessoaCod] = (pessoaNome, pessoaSalario)  # Inserção no dicionário...

    # Começa a ler outra pessoa:
    print("\nDigite um número não positivo para parar a leitura.")
    pessoaCod = int(input('Digite o código da pessoa: '))
print("\nFim da leitura de pessoas.\n")
salarioMaximo = float(input(f'Digite o salário máximo: '))
while salarioMaximo <= 0:
      salarioMaximo = float(input(f'Salário inválido. Digite um salário máximo positivo: '))

print("As pessoas que se enquadram nesse intervalo de salário são:")
contando = 0
soma = 0
for chave in pessoas:
    pessoaNome, pessoaSalario = pessoas[chave]
    if pessoaSalario < salarioMaximo:
        print(f"- {chave}, {pessoaNome}, {pessoaSalario} reais")
        contando += 1
        soma += pessoaSalario
if contando == 0:
      print("Não há pessoas com salário menos do que",salarioMaximo,"reais.")
else:
      print(f"A média de salários é de {soma/contando}")
      print(f"A quantidade de pessoas com o salário menor do que {salarioMaximo} reais é de {contando}.")

print("O Máximo Divisor Comum (MDC) de 2 números"
      "inteiros é o maior número inteiro que divide"
      "ambos sem deixar resto. Fazer um programa"
      "Python para: – Ler 2 números inteiros – verificar se são positivos."
      "– Ler 2 números inteiros – verificar se são positivos. "
      "– Determinar o MDC destes 2 números. "
      "– OBS: Não utilizar nenhuma fórmula matemática para calcular o MDC. "
      "Coloque o programa para trabalhar para você...")
n1 = int(input("Digite um número positivo: "))
while n1 <= 0:
      n1 = int(input("Número deve ser positivo. Digite um número positivo: "))
n2 = int(input("Digite outro número positivo: "))
while n2 <= 0:
      n2 = int(input("Número deve ser positivo. Digite um número positivo: "))
if n2 < n1:
      n1, n2 = n2, n1
mdc = 1
resto = n2 % n1
aux = n1
while resto != 0:
      aux2 = aux % resto
      aux = resto
      resto = aux2
mdc = aux
print(f"O MDC dos números {n1} e {n2} é {mdc}")

print("Fazer um programa Python para:"
      "– Ler um número inteiro positivo N digitado pelo usuário -"
      "o programa deve verificar se o valor de N é válido."
      "– Depois, ler N números inteiros positivos (0 < x < 4000)"
      "e, para cada um deles, imprimir a sua representação"
      "em algarismos romanos."
      "– Construir o resultado (valor em algarismos romanos)"
      "usando um String."
      "– OBS. Lembre que os valores dos algarismos romanos"
      "são: I=1, V=5, X=10, L=50, C=100, D=500, e M=1000,"
      "e que IV=4, IX=9, XL=40, XC=90, CD=400 e CM=900.")

x = int(input("Digite um número entre 0 e 4000: "))
while x <= 0 or x >= 4000:
    x = int(input("Número inválido. Digite um número entre 0 e 4000: "))
romano = ""
algarismos = {1000:'M', 900:'CM', 500:'D', 400:'CD',100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
for numero in algarismos:
    while x-numero >= 0:
        romano += algarismos[numero]
        x = x-numero
print(f"O número {x} em algarismos romanos é {romano}.")

print("Fazer um programa Python para:"
      "– Ler por linhas uma matriz M x N, onde M <= 4 e N <= 8 são lidos antes da leitura da matriz."
      "– Depois, percorrendo a matriz por colunas, armazenar em um vetor os elementos desta matriz que sejam"
      "múltiplos de 6."
      "– Finalmente, imprimir de maneira organizada a matriz e depois o vetor.")

m = int(input("Digite um número positivo menor ou igual a 4: "))
while m > 4 or m < 1:
    m = int(input("Digite um número positivo menor ou igual a 4: "))
n = int(input("Digite um número positivo menor ou igual a 8: "))
while n > 8 or n < 1:
    n = int(input("Digite um número positivo menor ou igual a 8: "))
matriz = []
multiplos = []
for i in range(m):
    matriz.append([0]*n)
# adicionando numeros a matriz
for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input("Digite um número: "))
for i in range(n):
    for j in range(m):
        if matriz[j][i] % 6 == 0:
            multiplos.append(matriz[j][i])
# imprimindo matriz
print("Matriz:")
for i in range(m):
    print(matriz[i])
# imprimingo multiplos
print("Elementos múltiplos de 6:",multiplos)