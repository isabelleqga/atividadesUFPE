# – Ler uma tabela com N profissões, onde
# • O valor de N é informado antes pelo usuário.
# • Cada profissão é formada por um código (número positivo) e um nome (String).
# • A leitura da tabela deve ser feita em uma subrotina.
# – Depois o usuário fornecerá uma lista de códigos para que o programa informe o nome de cada profissão.
# – Se o código da profissão não existir na tabela, mostrar a mensagem “Profissão Inexistente” e continuar.
# – O programa pára com a digitação de um código inválido (negativo ou zero).

def lerTabela(n):
    profissoes = {}
    for i in range(0,n):
        codigoProfissao = int(input("Digite o código da profissão: "))
        while codigoProfissao <= 0:
            codigoProfissao = int(input("Digite o código da profissão: "))
        nomeProfissao = input("Digite o nome da profissão: ")
        profissoes[codigoProfissao] = nomeProfissao
    print("Fim da leitura de profissões.\n")
    return profissoes

n = int(input("Digite o número de profissões da tabela: "))
while n <= 0:
    n = int(input("Número inválido. Digite o número de profissões da tabela: "))

profissoes = lerTabela(n)

cod = int(input("Digite um código para a pesquisa: "))
while cod <= 0:
    cod = int(input("Digite um código para a pesquisa: "))
while cod > 0:
    if cod in profissoes:
        nome = profissoes[cod]
        print(f"O código {cod} corresponde à profissão {nome}.\n")
    else:
        print("Profissão Inexistente.\n")
    cod = int(input("Digite um código para a pesquisa: "))


# – Faça uma subrotina Python do tipo função chamada MultiplicaDigitos, que receba um
# número Num inteiro positivo de 6 dígitos como parâmetro, e devolva a multiplicação dos
# dígitos não nulos deste número como resultado. Caso Num não seja positivo ou tenha mais de
# 6 dígitos significativos, a função deve retornar como resultado -1 ou -2, respectivamente.
#  Dica - O resto da divisão de um número por 10 retorna o dígito mais à direita, enquanto que a
#  divisão inteira dele por 10 retorna a outra parte. Ex: 1234 % 10 -> 4 e 1234 // 10 -> 123.
#  Este processo pode ser repetido para recuperar cada um dos dígitos de qualquer número.
# OBS - Você pode (ou não) incluir um programa principal para ler um valor de N e testar a sua
#  função: somente a função será avaliada na correção.

def MultiplicaDigitos (num):
    resultado = 1
    if num < 0:
        resultado = -1
    elif num > 999999:
        resultado = -2
    else:
        algarismos = [0]*6
        for i in range(0, 5):
            algarismos[i] = num % 10
            num = num // 10
            if algarismos[i] != 0:
                resultado *= algarismos[i]
    return resultado

print(f"O resultado é {MultiplicaDigitos(1245)}")

# Faça uma subrotina Python do tipo função recursiva para calcular a soma dos N primeiros
# termos da série abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o
# resultado da função. Observe que o símbolo “!” se refere ao fatorial do número e também que
# você não pode usar os comandos de repetição nesta questão.
# S = 3 + 5 / 2! + 15 / 3! + 30 / 4! + 75 / 5! + 180 / 6! + ...
# OBS - Você pode (ou não) incluir um programa principal para ler um valor de N e testar a sua
#  função: somente a função será avaliada na correção.

def funcaoRecursiva(n, numeradorImpar = 3, numeradorPar = 5, denominador = 1, imparOuPar = 1, aux = 1):
    aux += 1
    if imparOuPar == 1:
        soma = numeradorImpar / denominador
        if n > 1:
            soma += funcaoRecursiva(n-1, numeradorImpar * 5, numeradorPar, denominador*aux, -1, aux)
    else:
        soma = numeradorPar / denominador
        if n > 1:
            soma += funcaoRecursiva(n-1, numeradorImpar, numeradorPar * 6, denominador*aux, 1, aux)
    return soma

print(f"O resultado é {funcaoRecursiva(4)}")


# Faça uma subrotina Python do tipo Procedimento chamada MelhoresClientes para:

#  (a) ler um arquivo texto, cujo nome externo é formado a partir do nome de uma empresa,
# recebido como parâmetro, seguido da extensão '.txt'. O arquivo conterá as informações dos
# clientes do programa de fidelidade desta empresa, a saber: matrícula (inteiro com 5 dígitos),
# sexo (1=masculino ou 2=feminino), número de pontos (inteiro com 7 dígitos), e nome do
# cliente (string com 35 posições). Arquivo exemplo será fornecido juntamente com a questão.

#  (b) Gravar um arquivo, cujo nome externo é 'Melhores' concatenado após o nome da empresa,
# seguido da extensão '.txt', contendo somente a matrícula e o total de pontos (um cliente por
# linha) dos clientes com pontuação acima de um dado valor recebido como segundo parâmetro
# na subrotina. Ou seja, este procedimento deve ter 2 parâmetros.

#  (c) No final, o procedimento deve imprimir (na tela do terminal) um resumo das informações
# gravadas no arquivo contendo o nome da empresa, o número de registros gravados no arquivo
# e a média das pontuações destes melhores clientes.

#  Faça também um programa principal que leia o nome da empresa e o total de pontos a ser
# considerado na escolha dos melhores clientes de N empresas, com N informado no início pelo
# usuário, e faça uso do procedimento MelhoresClientes para cada uma delas. Caso ocorra erro
# no arquivo de alguma das empresas, o seu programa deve informar o usuário e desconsiderar
# esta empresa, possivelmente continuando a executar com outras empresas.

def MelhoresClientes (nomeEmpresa, pontosMelhores):
    try:
        soma = 0
        cont = 0
        print("Informações do arquivo: ")
        with open(nomeEmpresa+".txt",'r') as arquivo:
            for valor in arquivo:
                matricula, sexo, pontos, nome = valor.split(" ")
                pontos = int(pontos)
                if pontos > pontosMelhores:
                    with open(nomeEmpresa + "Melhores.txt", 'a') as arquivo2:
                        arquivo2.write(matricula + " " + str(pontos) + "\n")
                        soma += pontos
                        cont += 1
                print(valor)
        media = soma/cont
        print(f"\nNesse arquivo há informações de {cont} clientes.")
        print(f"\nA média de pontuações dos melhores clientes é de {media}.")
    except FileNotFoundError as mens:
        print("Erro", mens)

n = int(input("Digite quantas empresas você deseja pesquisar: "))
for i in range (n):
    nome = input("Digite o nome da empresa: ")
    pontos = int(input("Digite o número de pontos dos melhores clientes: "))
    MelhoresClientes(nome, pontos)

# A média ponderada de N números é a soma dos produtos de cada um deles multiplicados
# por seus respectivos pesos; o resultado dessa soma é então dividido pela soma dos pesos. A
# média ponderada é utilizada em diversas disciplinas para calcular os resultados dos alunos
# considerando duas avaliações parciais com pesos variáveis. As regras para definição do
# resultado são as seguintes:
# • Se a média do aluno for maior ou igual a sete, o aluno “está aprovado”.
# • Se a média do aluno for menor que três, o aluno “está reprovado”.
# • Se a média do aluno for menor que sete e maior ou igual a três, ele “fará prova final”.

# Faça uma subrotina Python do tipo procedimento que (a) receba o nome de um único aluno
# como parâmetro, (b) leia as notas das duas avaliações parciais desse aluno, (c) calcule sua média,
# e (d) imprima seu resultado como: "O aluno __________ obteve média ____ e __________."
# OBS - Os pesos utilizados no procedimento (peso1 e peso2) são parâmetros opcionalmente
#  recebidos na chamada e, se não forem informados, seus valores devem ser 1.
# OBS2 - Você pode (ou não) incluir um programa principal para testar a sua subrotina: somente a
#  função será avaliada na correção.

def calcularMedia (nomeAluno, peso1 = 1, peso2 = 1):
    fim = False
    nota1_valida = False
    while not fim:
        try:
            if not nota1_valida:
                nota1 = float(input("Digite a nota da primeira prova: "))
                while (nota1 < 0) or (nota1 > 10):
                    nota1 = float(input("Nota inválida. Digite a nota da primeira prova: "))
                nota1_valida = True
            nota2 = float(input("Digite a nota da segunda prova: "))
            while (nota2 < 0) or (nota2 > 10):
                nota2 = float(input("Nota inválida. Digite a nota da segunda prova: "))
        except ValueError:
            print("Nota inválida. O valor digitado deve ser um número.")
        else:
            fim = True
    media = (nota1*peso1 + nota2*peso2) / (peso1+peso2)
    if media >= 7:
        res = "está aprovado"
    elif media < 3:
        res = "está reprovado"
    elif (media >= 3) and (media < 7):
        res = "fará prova final"
    print(f"O aluno {nomeAluno} obteve média {media} e {res}.")

calcularMedia("Arthur",1,7)
calcularMedia("Bea",1,4)
calcularMedia("Carla")
calcularMedia("Dentista")


# Faça uma subrotina Python do tipo função recursiva para calcular a soma dos N primeiros
# termos da série abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o
# resultado da função.
# S = 105 / 25 – 130 / 35 + 140 / 45 – 160 / 55 + 175 / 65 – 190 / 75 ....
# OBS1 - Observe que você não pode usar os comandos de repetição nesta questão.
# OBS2 - Você pode (ou não) incluir um programa principal para testar a sua função: somente
#  a função será avaliada na correção.

def funcaoRecursiva(n, numeradorImpar = 105, numeradorPar = 130, denominador = 25, sinal = 1):
    if sinal == 1:
        soma = sinal * numeradorImpar / denominador
        if n > 1:
            soma += funcaoRecursiva(n-1, numeradorImpar + 35, numeradorPar, denominador+10, -1)
    else:
        soma = sinal * numeradorPar / denominador
        if n > 1:
            soma += funcaoRecursiva(n-1, numeradorImpar, numeradorPar + 30, denominador+10, 1)
    return soma

print(f"O resultado é {funcaoRecursiva(4)}")


# Considere um arquivo texto, cujo nome externo deve ser informado pelo usuário no início,
# contendo as informações dos materiais/estoque da empresa: código (inteiro com 3 posições),
# nome (string com 20 posições), qtdMinima e qtdAtual (ambos inteiros com 4 posições).

# Assuma que tem um espaço em branco separando as informações e que tem um material em
# cada linha do arquivo. Faça um programa Python para ler este arquivo e gravar o arquivo
# texto ‘compras.txt’, contendo informações das compras, também um material por linha:
# código, nome, e qtdCompra (inteiro com 4 posições), que precisam ser feitas para repor o
# estoque, apenas dos materiais que estejam com estoque abaixo do mínimo.

# Você deve escrever e usar uma função calculaCompra que deve receber como parâmetros o
# estoque mínimo e o estoque atual, e retornar como resultado a quantidade a ser comprada. A
# quantidade a ser comprada deve satisfazer a:
# (a) Os materiais que estejam com menos da metade do estoque mínimo devem fazer compras
# para ficar com estoque 20% acima do estoque mínimo.
# (b) Os materiais que estejam com estoque entre 50% e 90% (inclusive) do estoque mínimo
# devem fazer compras para ficar com estoque 10% acima do mínimo.
# (c) Os materiais que estejam com estoque de mais de 90% do estoque mínimo devem fazer
# compras apenas para repor este estoque mínimo.
# OBS - Eventuais valores decimais resultantes das operações envolvendo percentuais devem
#  ser truncados (desprezados).


def calculaCompra(qtdMinima, qtdAtual):
    if qtdAtual < qtdMinima/2:
        res = qtdMinima*1.2 - qtdAtual
    if (qtdAtual <= qtdMinima*0.9) and (qtdAtual >= qtdMinima*0.5):
        res = qtdMinima * 1.1 - qtdAtual
    if qtdAtual > qtdMinima*0.9:
        res = qtdMinima - qtdAtual
    return res

fim = False
while not fim:
    try:
        nome = input("Digite o nome da empresa: ")
        leitura = open(nome + ".txt", 'r')
        escrita = open("compras.txt", 'w')
        for valor in leitura:
            codigo = valor[0:3]
            nome = valor[4:24]
            qtdMinima = valor[25:29]
            qtdAtual = valor[30:34]
            qtdMinima = int(qtdMinima)
            qtdAtual = int(qtdAtual)
            if qtdAtual < qtdMinima:
                qtdCompra = calculaCompra(qtdMinima, qtdAtual)
                escrita.write(codigo + " " + nome + " " + str(qtdCompra) + "\n")
        leitura.close()
        escrita.close()
    except FileNotFoundError as mens:
        print(mens)
    else:
        print("Sucesso")
        fim = True

# Q1 – Faça uma função Python para calcular a soma dos N primeiros termos da série abaixo. O
# valor de N deve ser um parâmetro e a função deve retornar zero como resultado caso o
# número de termos não seja positivo.
# S = 150 / 4 – 95 / 11 + 158 / 5 – 100 / 14 + 166 / 6 – 105 / 17 + ...
# Escreva também um programa principal para perguntar ao usuário a quantidade de vezes (qtd)
# que ele deseja calcular o valor da série e, em seguida, os números de termos desejados nestas
# qtd vezes. Para cada um deles, seu programa deve usar a função acima e imprimir o resultado
# da série (com 4 casas decimais), da seguinte forma: “O valor da série com ... termos é ...”.
# OBS: A impressão destes resultados deve ser feita em ordem decrescente dos números de
# termos (digitados pelo usuário).

def funcao(n):
    s = 0
    numeradorImpar = 150
    denominadorImpar = 4
    numeradorPar = 95
    denominadorPar = 11
    if n <= 0:
        return 0
    else:
        for i in range(1, n + 1):
            if i % 2 != 0:
                s += numeradorImpar / denominadorImpar
                numeradorImpar += 8
                denominadorImpar += 1
            else:
                s -= numeradorPar / denominadorPar
                numeradorPar += 5
                denominadorPar += 3
        return s

qtd = int(input("Digite o número de vezes que deseja calcular o valor da série:"))
while qtd <= 0:
    qtd = int(input("Quantidade inválida. Digite o número de vezes que deseja calcular o valor da série:"))
numeros = [0]*qtd
for i in range(0,qtd):
    n = int(input("Digite o número de termos:"))
    numeros[i] = n

numeros.sort()
numeros = list(reversed(numeros))
for i in range (0,qtd):
    print(f"O valor da série com {numeros[i]} termos é {round(funcao(numeros[i]), 4)}")


# Q2 – Faça um programa Python para, a partir de informações digitadas pelo usuário, criar um
# arquivo texto de disciplinas, uma disciplina por linha, contendo códigos (string, tamanho 5),
# nomes (string, tamanho 25), e cargas horárias (int, tamanho 3). O nome do arquivo deve ser
# informado pelo usuário no início. A digitação dos dados deve parar quando o usuário digitar
# "FIM" no código da disciplina, i.e., ele não informará o número de disciplinas que digitará.
#  O seu programa deve ter também uma subrotina do tipo procedimento, chamada no final,
# para imprimir, a partir de informações recebidas em parâmetros, a quantidade de registros e a
# média das cargas horárias das disciplinas gravadas no arquivo, bem como a quantidade de
# disciplinas com carga horária maior do que 60 horas.

def ler(nome):
    leitura = open(nome + ".txt", 'r')
    cont = 0
    soma = 0
    cont2 = 0
    for valor in leitura:
        cont += 1
        carga = valor[30:]
        carga = int(carga)
        soma += carga
        if carga > 60:
            cont2 += 1
    media = soma/cont
    print(f"Quantidade de disciplinas: {cont}")
    print(f"Média das cargas: {media}")
    print(f"Quantidade de disciplinas com mais de 60 horas: {cont2}")


nome = input("Digite o nome do arquivo:")
fim = False
while not fim:
    try:
        escrita = open(nome + ".txt", 'w')
        discCodigo = input("Digite o código da disciplina:")
        while discCodigo != 'FIM':
            discNome = input("Digite o nome da disciplina:")
            discCarga = input("Digite a carga horária da disciplina:")
            escrita.write(f'{discCodigo:5} {discNome:25} {discCarga:3}\n')
            discCodigo = input("Digite o código da disciplina:")
        escrita.close()
        ler(nome)
    except FileNotFoundError as mens:
        print(mens)
    else:
        print("Sucesso")
        fim = True



# Faça uma função Python para calcular a soma dos N primeiros termos da série abaixo. O
# valor de N deve ser um parâmetro e a função deve retornar zero como resultado caso o
# número de termos não seja positivo.
# S = 150 / 4 – 145 / 9 + 140 / 6 – 135 / 13 + 130 / 8 – 125 / 17 + ...
# Escreva também um programa principal para repetidamente perguntar ao usuário o número de
# termos desejado: o programa deve parar quando o usuário informar um número que não seja
# positivo. Para cada um deles, seu programa deve usar a função acima e imprimir o resultado
# da série (com 3 casas decimais), da seguinte forma: “A série com ... termos totaliza ...”

def funcao (n):
    if n <= 0:
        return 0
    else:
        s = 0
        numImpar = 150
        denImpar = 4
        numPar = 145
        denPar = 9
        for i in range(1, n+1):
            if i % 2 != 0:
                s += numImpar/denImpar
                numImpar -= 10
                denImpar += 2
            else:
                s -= numPar/denPar
                numPar -= 10
                denPar += 4
        return s

n = int(input("Digite o número de termos: "))
while n <= 0:
    n = int(input("Inválido. Digite o número de termos: "))
while n > 0:
    print(f"A série com {n} termos totaliza {round(funcao(n),3)}\n")
    n = int(input("Digite o número de termos: "))

# Faça um programa Python para ler (no programa principal) uma seqüência de números
# inteiros múltiplos de 7 – a leitura pára quando o número zero for lido. No entanto, o usuário
# só poderá digitar no máximo 100 números válidos. O programa deve possuir uma subrotina
# do tipo procedimento para imprimir as seguintes informações como resultado (nesta ordem):
#  Os números lidos que também sejam múltiplos de 5.
#  Os números lidos que não sejam múltiplos de 11.

def imprime_mult(num_lst, qtd):
    m5 = []
    m11 = []
    for i in range(qtd):
        if num_lst[i] % 5 == 0:
            m5.append(num_lst[i])
        if num_lst[i] % 11 != 0:
            m11.append(num_lst[i])

    if len(m5) == 0:
        print("Nenhum múltiplo de 5 encontrado.")
    else:
        print(f"Números múltiplos de 5: {m5}")

    if len(m11) == 0:
        print("Nenhum não múltiplo de 11 encontrado.")
    else:
        print(f"Números não múltiplos de 11: {m11}")

num_lista = [0] * 100
qtd = 0
fim = False
while not fim:
    try:
        num = int(input("Digite um número inteiro múltiplo de 7: "))
        while (num % 7 != 0) and (num != 0):
            num = int(input("O número digitado não é múltiplo de 7. Digite um número inteiro múltiplo de 7: "))
        while (num != 0) and (qtd < 10):
            num_lista[qtd] = num
            qtd += 1
            num = int(input("Digite um número inteiro múltiplo de 7: "))
            while (num % 7 != 0) and (num != 0):
                num = int(input("O número digitado não é múltiplo de 7. Digite um número inteiro múltiplo de 7: "))

        if qtd == 0:
            print("Nenhum número múltiplo de 7 foi digitado.")
        else:
            imprime_mult(num_lista, qtd)
    except ValueError:
        print("Erro. Valor inconsistente.")
    else:
        fim = True

# Considere um arquivo texto com nome externo 'clientes.arq', com informações dos clientes
# do programa de fidelidade de uma dada empresa, contendo: matrícula (inteiro, 4 posições),
# nome (string, 30 posições), sexo ('M' ou 'F'), e pontos (inteiro, 5 posições).
# Faça um programa Python para ler o arquivo acima e imprimir a matrícula e o total de pontos
# dos clientes com pontuação acima de um dado valor mínimo informado pelo usuário no início
# do programa (este valor mínimo deve ser maior que 1000).
#
#  No final, o programa deve imprimir ainda (a) o número de registros lidos, (b) o número de
# clientes impressos, e (c) a média das pontuações destes clientes.

fim = False
while not fim:
    try:
        valorminimo = int(input("Digite o valor mínimo de pontos:"))
        while valorminimo < 1000:
            valorminimo = int(input("Valor inválido. Digite o valor mínimo de pontos:"))

        leitura = open("clientes.txt", "r")
        cont = 0
        cont2 = 0
        soma = 0
        print(f"Os clientes com mais de {valorminimo} pontos são:")
        for valor in leitura:
            matricula = valor[0:4]
            pontos = valor[38:]
            cont += 1
            if int(pontos) > valorminimo:
                print(f"{matricula} {pontos}", end="")
                cont2 += 1
                soma += int(pontos)
        print(f"\nO total de clientes lidos: {cont}")
        print(f"O total de clientes impressos: {cont2}")
        print(f"A média de pontuação dos clientes lidos: {soma / cont2}")
        leitura.close()
    except ValueError:
        print("O valor mínimo digitado deve ser um número inteiro.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    else:
        print("Programa finalizado.")
        fim = True


# Considere um arquivo texto com nome externo 'discip.txt', contendo informações de disciplinas:
# código com 5 posições, nome com 35 posições, créditos com 2 posições, e código do centro a que pertence com 3 posições;
# uma disciplina por linha.
# Considere também um outro arquivo texto nome externo 'centros.txt', contendo informações de centros:
# código com 3 posições e nome com 25 posições; também um centro por linha.

# Faça um programa Python para:
# – Usando um procedimento, ler o arquivo de centros e colocar seu conteúdo em uma tabela.
# – Gravar um arquivo texto com nome externo 'discipCompleto.txt', contendo todas as informações do
# arquivo 'discip.txt' e mais o nome do centro a que pertence.
# – Escrever uma função para achar o nome do centro a partir do seu código.
# – No final imprimir a quantidade de disciplinas e de centros.

def leitura(centros):
    with open('centros.txt', 'r') as leitura:
        for linha in leitura:
            codigo = linha[0:3]
            centro = linha[4:29]
            centros[codigo] = centro

fim = False
while not fim:
    try:
        cont = 0
        centros = {}
        leitura(centros)
        escrita = open("discipCompleto.txt","w")
        leitura2 = open("discip.txt", 'r')
        for valor2 in leitura2:
            codigo2 = valor2[0:5]
            nome2 = valor2[6:41]
            creditos2 = valor2[42:44]
            cod_centro = valor2[45:48]
            nomedocentro = centros[cod_centro]
            escrita.write(f"{codigo2} {nome2} {creditos2} {cod_centro} {centros[cod_centro]}")
            cont += 1
        leitura2.close()
        escrita.close()
    except FileNotFoundError as msg:
        print(msg)
    except PermissionError:
        print("Sem permissão de escrita.")
    else:
        fim = True
        print(f"Quantidade de disciplinas: {cont}\nQuantidade de centros: {len(centros)}")

# Faça um programa para ler o arquivo "titanic.txt" e armazenar o nome, o sexo e a idade
# de todos os passageiros sobreviventes em "sobreviventes.txt". Ao final do programa
# imprima na tela:
# 1) a quantidade de sobreviventes homens;
# 2) a quantidade de sobreviventes mulheres; e
# 3) a média de idade de todos os sobreviventes.

fim = False
while not fim:
    try:
        leitura = open("titanic.txt", "r")
        escrita = open("sobreviventes.txt", "w")
        media = 0.0
        contMulheres = 0
        contHomens = 0
        for valor in leitura:
            colunas = valor.split(',')
            if colunas[1] == '1':
                nome = colunas[3]
                sexo = colunas[4]
                idade = colunas[5]
                if sexo == 'male':
                    contHomens += 1
                else:
                    contMulheres += 1
                media += float(idade)
                escrita.write(f'{nome},{sexo},{idade}\n')
        leitura.close()
        escrita.close()

    except FileNotFoundError as msg:
        print(msg)
    except PermissionError:
        print("Sem permissão de escrita.")
    else:
        fim = True
        print(f"Quantidade de mulheres que sobreviveram: {contMulheres}")
        print(f"Quantidade de homens que sobreviveram: {contHomens}")
        media = media / (contHomens + contMulheres)
        print(f"Média da idade dos sobreviventes: {media:.2f}")