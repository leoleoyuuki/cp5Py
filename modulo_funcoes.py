from random import randint
def cria_bingo_aleatorio(lin,col):
    matriz = []
    sorteados = []
    for i in range(lin):
        linha = []
        for j in range(col):
            if j == 0:
                n = randint(1,10)
                while n in sorteados:
                    n = randint(1,10)
                linha.append(n)
                sorteados.append(n)
            if j == 1:
                n = randint(11,20)
                while n in sorteados:
                    n = randint(11,20)
                linha.append(n)
                sorteados.append(n)
            if j == 2:
                n = randint(21,30)
                while n in sorteados:
                    n = randint(21,30)
                linha.append(n)
                sorteados.append(n)
            if j == 3:
                n = randint(31,40)
                while n in sorteados:
                    n = randint(31,40)
                linha.append(n)
                sorteados.append(n)
            if j == 4:
                n = randint(41,50)
                while n in sorteados:
                    n = randint(41,50)
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


resposta = cria_bingo_aleatorio(5,5)
exibe_matriz(resposta)