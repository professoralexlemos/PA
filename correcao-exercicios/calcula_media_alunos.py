"""Considere uma turma com 10 alunos, cada um com 4 notas. Estes dados são  armazenados em uma matriz 10 x 6, em que a primeira coluna armazena a matrícula do aluno e as 4 últimas armazenam as suas notas. Fazer um algoritmo que:
        a) Leia estes dados, armazenando-os;
        b) Imprima a média de cada aluno;
        c) Imprima a maior média e a matrícula do aluno que a possui;

Responsabilidades
1) - Vamos ler as informações dos alunos[ler a matricula e as notas];
2) - Calcular a média do Aluno;
3) - Verificar qual a maior média;
4) - Exibir a maior média e a matricula do aluno;

Funções
1) - Vamos ler as informações dos alunos[ler a matricula e as notas];
     ENTRADA [matriz vazia para guardar informações dos alunos]
     PROCESSAMENTO [preencher a matriz com as informações dos aluno, o usuário irá informar os dados]
     SAÍDA[retornar a matriz com os dados dos alunos preenchidos]

2) - Calcular a média do Aluno;
     ENTRADA [as quatro notas do aluno]
     PROCESSAMENTO [calcular a média, soma as 4 notas e divide por 4]
     SAÍDA [a média calculada]

3) - Verificar qual a maior média;
     ENTRADA [todas as médias dos aluno]
     PROCESSAMENTO [descobrir a maior média]
     SAÍDA [retornar a maior média encontrada]

4) - Exibir a maior média e a matrícula do aluno;
     ENTRADA [a maior média e a matrícula do aluno]
     PROCESSAMENTO []
     SAÍDA [não tem retorno]
"""

# funcoes

'''1) - Vamos ler as informações dos alunos[ler a matricula e as notas];
     ENTRADA [matriz vazia para guardar informações dos alunos]
     PROCESSAMENTO [preencher a matriz com as informações dos aluno, o usuário irá informar os dados]
     SAÍDA[retornar a matriz com os dados dos alunos preenchidos]'''
def popula_dados_alunos(alunos):
    dados = []
    '''for linha in range(0, 10, 1):
        dados = []
        for coluna in range(0, 5, 1):
            if coluna == 0:
                print("-" * 20)
                dados.append(int(input("Informe a matricula do aluno: ")))
            else:
                dados.append(float(input(f"Informe a {coluna}ª nota do aluno: ")))
        alunos.append(dados)

        return alunos'''
    return [[100, 5, 5, 5, 5], [200, 6, 5, 5, 5], [300, 3, 5, 5, 5]]


'''
2) - Calcular a média do Aluno;
     ENTRADA [as quatro notas do aluno]
     PROCESSAMENTO [calcular a média, soma as 4 notas e divide por 4]
     SAÍDA [a média calculada]
'''
def calcular_media_aluno(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4


'''
3) - Verificar qual a maior média;
     ENTRADA [todas as médias dos aluno]
     PROCESSAMENTO [descobrir a maior média]
     SAÍDA [retornar a maior média encontrada]
'''
def verifica_maior_media_alunos(alunos):
    maior_media = 0
    for linha in range(3):
        media = alunos[linha][5]
        if media > maior_media:
            maior_media = media
    return maior_media

'''
4) - Exibir a maior média e a matrícula do aluno;
     ENTRADA [a maior média e a matrícula do aluno]
     PROCESSAMENTO []
     SAÍDA [não tem retorno]
'''
def exibe_maior_media_e_matricula(media, matricula):
    print(f'A maior média foi {media} do aluno com matrícula: {matricula}')

# variaveis
alunos = []

# programa principal
alunos = popula_dados_alunos(alunos)

for linha in range(3):
    media = calcular_media_aluno(alunos[linha][1], alunos[linha][2], alunos[linha][3], alunos[linha][2])
    alunos[linha].append(media)

maior_media = verifica_maior_media_alunos(alunos)

for linha in range(3):
    if alunos[linha][5] == maior_media:
        exibe_maior_media_e_matricula(maior_media, alunos[linha][0])
