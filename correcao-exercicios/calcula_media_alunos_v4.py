"""Considere uma turma com vários alunos, cada um com 4 notas. Estes dados são  armazenados em uma matriz, em que a primeira coluna armazena a matrícula do aluno e as 4 últimas armazenam as suas notas. Fazer um algoritmo que:
        a) Leia estes dados, armazenando-os;
        b) Imprima a média de cada aluno;
        c) Imprima a maior média e a matrícula do aluno que a possui;"""


def popula_dados_alunos():
    """
    Popula os dados dos alunos
    :return: Matriz com os dados dos alunos
    """
    continuar = True
    alunos = []
    while continuar:
        dados = []
        for coluna in range(indice_media):
            if coluna == 0:
                exibe_caracter('-', 35)
                dados.append(int(input("Informe a matricula do aluno: ")))
            else:
                dados.append(float(input(f"Informe a {coluna}ª nota do aluno: ")))
        alunos.append(dados)
        continuar = input('Digite S para CONTINUAR ou qualquer tecla para sair: ').upper() == 'S'
    return alunos


def popula_medias_alunos(alunos):
    """
    Popula as médias dos alunos
    :param alunos:
    :return: Matriz com os dados das médias dos alunos
    """
    nota1 = 1
    nota2 = 2
    nota3 = 3
    nota4 = 4
    for indice_aluno in range(len(alunos)):
        media = (alunos[indice_aluno][nota1] + alunos[indice_aluno][nota2] + alunos[indice_aluno][nota3] + alunos[indice_aluno][nota4]) / 4
        alunos[indice_aluno].append(media)
    return alunos


def calcula_maior_media_alunos(alunos):
    """
    Calcula a maior média dos alunos
    :param alunos: Os dados das alunos
    :return: A maior média dos alunos
    """
    maior_media = 0
    for indice_aluno in range(len(alunos)):
        media = alunos[indice_aluno][indice_media]
        if media > maior_media:
            maior_media = media
    return maior_media


def exibe_maior_media_e_matricula(alunos, maior_media):
    """
    Exibe a maior média calcula e a matrícula dos alunos
    :param alunos: Os dados do alunos
    :param maior_media: A maior média calculada dos alunos
    """
    for indice_aluno in range(len(alunos)):
        if alunos[indice_aluno][indice_media] == maior_media:
            exibe_caracter('=', 55)
            print(f'A maior média calculada foi {alunos[indice_aluno][indice_media]} do aluno com a matrícula: {alunos[indice_aluno][indice_matricula]}')
            exibe_caracter('=', 55)
    exibe_caracter('-', 35)


def exibe_caracter(caracter, quantidade):
    """
    Exibe um caracter várias vezes, de acordo com o tamanho informado
    :param caracter: O caracter a ser exibido
    :param quantidade: A quantidade de exibição do caracter informado
    """
    print(caracter * quantidade)


# programa principal

alunos = []
indice_matricula = 0
indice_media = 5

alunos = popula_dados_alunos()
popula_medias_alunos(alunos)
exibe_maior_media_e_matricula(alunos, calcula_maior_media_alunos(alunos))
