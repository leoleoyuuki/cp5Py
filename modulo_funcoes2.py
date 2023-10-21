from random import randint

def cria_bingo_aleatorio(lin, col):
    matriz = []
    sorteados = []
    for i in range(lin):
        linha = []
        for j in range(col):
            if j == 0:
                n = randint(1, 10)
                while n in sorteados:
                    n = randint(1, 10)
                linha.append(n)
                sorteados.append(n)
            if j == 1:
                n = randint(11, 20)
                while n in sorteados:
                    n = randint(11, 20)
                linha.append(n)
                sorteados.append(n)
            if j == 2:
                n = randint(21, 30)
                while n in sorteados:
                    n = randint(21, 30)
                linha.append(n)
                sorteados.append(n)
            if j == 3:
                n = randint(31, 40)
                while n in sorteados:
                    n = randint(31, 40)
                linha.append(n)
                sorteados.append(n)
            if j == 4:
                n = randint(41, 50)
                while n in sorteados:
                    n = randint(41, 50)
                linha.append(n)
                sorteados.append(n)
        matriz.append(linha)
    return matriz

def exibe_matriz(matriz: list) -> None:
    '''Exibe a matriz'''
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()


def inicio_de_jogo():
    print('Bem-vindo ao Bingo!')
    while True:
        try:
            nm_jogadores = int(input('Quantos jogadores de 1 a 5? '))
            if 1 <= nm_jogadores <= 5:
                return nm_jogadores
            else:
                print('Por favor, digite um número entre 1 e 5 jogadores!')
        except ValueError:
            print('Entrada inválida')

def solicita_nomes(nm_jogadores):
    nomes_jogadores = []
    for i in range(nm_jogadores):
        nome = input(f'Nome do {i + 1}º jogador: ')
        nomes_jogadores.append(nome)
    return nomes_jogadores

nm_jogadores = inicio_de_jogo()

nomes_jogadores = solicita_nomes(nm_jogadores)

print("Nomes dos jogadores:")
for i, nome in enumerate(nomes_jogadores):
    print(f'Jogador {i + 1} - {nome}')

def sorteia_numero(sorteio_bingo):
    nb = randint(1, 50)
    while nb in sorteio_bingo:
        nb = randint(1, 50)
    sorteio_bingo.append(nb)
    return sorteio_bingo

sorteio_bingo = [] 
sorteio_bingo = sorteia_numero(sorteio_bingo)
print(sorteio_bingo)


