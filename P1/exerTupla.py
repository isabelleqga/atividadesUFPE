
print("1. Fazer um programa para:"
      "\nLer uma tabela com Cursos, onde:"
      "\nCada curso é formado por um código (número positivo), um nome (String), e o centro a que pertence (número positivo)."
      "\nA leitura da tabela de cursos para com o código de curso zero."
      "\nDepois o usuário fornecerá uma lista de códigos de centro para que o programa imprima o código e nome"
      "de todos os cursos associados a cada centro digitado."
      "\nSe o código do centro não existir na tabela, mostrar a mensagem “Nenhum curso encontrado” e continuar."
      "\nO programa pára com a digitação de um código de centro inválido (negativo ou zero).\n")
areas = {100:"Exatas", 200:"Biológicas", 300:"Artes", 400:"Informática", 500:"Engenharia"}
cursos = {}
cursoCod = int(input('Digite o código do curso: '))
while (not isinstance(cursoCod, int)) or (cursoCod <= 0) :
    cursoCod = int(input('O primeiro código não pode ser menor que 1. Digite o código do curso: '))
while cursoCod != 0:
    cursoNome = input(f'Digite o nome do curso {cursoCod}:')
    print("Áreas disponíveis:", areas)
    cursoArea = int(input(f'Digite a área do curso {cursoCod}:'))
    while not(cursoArea in areas):  # Verifica se a área existe...
        cursoArea = int(input(f'Área inexistente. Digite uma área válida para o {cursoCod}:'))
    cursos[cursoCod] = (cursoNome, cursoArea)  # Inserção no dicionário...

    # Começa a ler outro curso:
    print("\nDigite 0 para parar a leitura.")
    cursoCod = int(input('Digite o código do curso: '))
    while cursoCod in cursos or cursoCod < 0:
        cursoCod = int(input('Código inválido. Digite o código do curso: '))
print('Visualizar cursos: ', cursos, "\n")

areaCod = int(input('Digite um código de área para mostrar seus cursos (<=0 para parar): '))
while areaCod > 0:
    if areaCod in areas:
        print(f"\nA área {areaCod} possui os seguintes cursos:")
        for chave in cursos:
            cursoNome, cursoArea = cursos[chave]
            if cursoArea == areaCod:
                print(f"- {chave}, {cursoNome}")
    else:
        print("Nenhum curso encontrado.")
    areaCod = int(input('\nDigite um código de área para mostrar seus cursos (<=0 para parar): '))

