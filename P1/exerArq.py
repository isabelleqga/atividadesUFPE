# #1. Fazer um programa para:
# – Ler um arquivo com profissões, onde cada profissão é formada por um código
# (positivo) e um nome (String), uma profissão por linha.
# – Receber do usuário uma lista de códigos para que o programa informe o nome de cada profissão.
# – Se o código da profissão não existir no arquivo, mostrar a
# mensagem “Profissão Inexistente”, gravar em outro arquivo estes códigos de profissões, e continuar.
# – O programa pára com a digitação de um código inválido (negativo ou zero).
fim = False
while not fim:
    try:
        codigopesquisa = int(input("Digite o código da profissão que você deseja pesquisar:"))
        while codigopesquisa > 0:
            leitura = open("profissoes.txt", "r")
            achou = False
            for valor in leitura:
                codigo, nome = valor.split(" ")
                if int(codigo) == codigopesquisa:
                    print(f"A profissão de código {codigopesquisa} é {nome}")
                    achou = True
            if not achou:
                print("Profissão Inexistente")
                with open("profissoesinexistentes.txt", "a") as escrita:
                    escrita.write(str(codigopesquisa)+"\n")
            leitura.close()
            codigopesquisa = int(input("Digite o código da profissão que você deseja pesquisar:"))
    except ValueError:
        print("Código inválido.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    else:
        fim = True

# 1. Considere um arquivo texto com nome externo ´discipold.txt´, contendo informações de disciplinas
# (Código com 5 posições, nome com 35 posições e créditos com 2 posições), uma disciplina por linha. Faça
# um programa Python para criar um segundo arquivo com nome externo ´discipnew.txt´ contendo
# informações das mesmas disciplinas, mas com as seguintes modificações:

# – As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas, i.e., não devem ser gravadas no novo arquivo.
# – Os números de créditos das disciplinas cujos códigos começam por MA devem ser alterados para 5.
# – O novo arquivo terá um campo a mais (carga horária, com 3 posições) cujo valor deve ser o número
# de créditos da disciplina multiplicado por 15.
# No final o seu programa deve imprimir o número de disciplinas de cada arquivo e também o número de
# disciplinas que tiveram seus números de créditos alterados.

try:
    escrita = open("discipnew.txt", "w")
    leitura = open("discipold.txt", "r")
    creditoalterado = 0
    contdisciplinas = 0
    contdisciplinasnovas = 0
    for valor in leitura:
        codigo = valor[0:5]
        nome = valor[6:41]
        creditos = valor[42:44]
        contdisciplinas += 1
        if (codigo != 'IF125') and (codigo != 'IF380'):
            contdisciplinasnovas += 1
            if codigo[0:2] == 'MA':
                creditos = 5
                creditoalterado += 1
            cargahoraria = int(creditos)*15
            escrita.write(f"{codigo} {nome} {creditos:2} {str(cargahoraria):3}\n")
    escrita.close()
except FileNotFoundError:
    print("Erro. Arquivo não encontrado.")
except PermissionError:
    print("Erro. Sem permissão de acesso/criação de arquivo.")
else:
    print(f"Número de disciplinas em old: {contdisciplinas}")
    print(f"Número de disciplinas em new: {contdisciplinasnovas}")
    print(f"Número de disciplinas alteradas: {creditoalterado}")