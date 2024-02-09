
def calculo(n, nu=10, de=1, de1=5):
    soma = nu/de
    if (nu//2) % 2 == 0:
        soma = - nu/de1
    if n > 1:
        if (nu//2) % 2 == 0:
            soma += calculo(n-1, nu+2, de, de1+6)
        else:
            soma += calculo(n-1, nu+2, de+7, de1)
    return soma

n = int(input("Digite a quantidade de termos: "))
resposta = calculo(n)
print(resposta)

def procedimento(N, num = 10, denpos = 1, denneg = 5, sinal=1):
    if sinal == 1:
        soma = sinal * num / denpos
        if N > 1:
            soma += procedimento(N-1, num + 2, denpos + 7, denneg, -1)
    else:
        soma = sinal * num / denneg
        if N > 1:
            soma += procedimento(N-1, num + 2, denpos, denneg - 6, 1)
    return soma

# 1. Fazer subrotinas recursivas para calcular o valor das seguintes séries – com n termos,
# onde n deve ser um parâmetro recebido na chamada:
# – S2 = 37*38/1 - 36*37/2 + 35*36/3 – 34*35/4 + ...
# – S3 = 2/500 – 5/490 + 2/480 – 5/470 + ...
# • OBS: Mostrar como será a chamada externa do métodom, por exemplo, no prograa principal.

def subrotina1(n, numerador = 37, denominador = 1):
    s2 = (numerador * (numerador + 1)) / denominador
    if n > 1:
        s2 -= subrotina1(n - 1, numerador - 1, denominador + 1)
    return s2

def subrotina2(n, numerador = 2, denominador = 500):
    s3 = numerador/denominador
    if n%2 ==0:
        numerador = -5
    else:
        numerador = 2
    if n > 1:
        s3 += subrotina2(n - 1, numerador, denominador - 10)
    return s3

n = int(input("Digite o número de termos da sequência:"))
res = subrotina1(n)
res2 = subrotina2(n)
print(f"As sequências com {n} termos são {res} e {res2}")

# Fazer um programa para:
# – Ler números inteiros positivos digitados pelo usuário.
# • A leitura pára quando um número negativo for digitado.
# – Imprimir, para cada um deles, o termo equivalente na seqüência de Fibonacci.
# – Os números da seqüência de Fibonacci são:
# • 0, 1, 1, 2, 3, 5, ... Note que a partir do terceiro termo, cada termo é a soma dos 2 termos anteriores.
# – Usar uma subrotina que recebe o número do termo como parâmetro e retorna o seu valor.
# • implementá-la nas versões recursiva e não recursiva.

def fibonacci(n, t1 = 1, res = 0):
    if n > 1:
        res = fibonacci(n-1, res, t1+res)
    return res

n = int(input("Digite um número:"))
while n > 0:
    res = fibonacci(n)
    print(f"\nO termo {n} de Fibonacci é {res}.")
    n = int(input("Digite um número:"))

# S  =  2  –  7 / 5   +  8 / 3  –  13 / 9  +  32 / 9 – 19 / 13  + 128 / 27 ...


