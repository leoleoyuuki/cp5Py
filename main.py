# Leonardo Yuuki Nakazone - Rm550373
# Daniel Soares Delfin - Rm 552184


from random import randint

def inicio_de_jogo() -> int:

    """
        Inicia o jogo de Bingo, solicitando o número de jogadores de 1 a 5 e validando a entrada.

        Returns:
            int: O número de jogadores selecionado (entre 1 e 5).
    """

    print('Bem-vindo ao Bingo!')
    while True:
        try:
            nm_jogadores = int(input('Quantos jogadores de 1 a 5? '))
            if nm_jogadores >= 1 and nm_jogadores <= 5:
                return nm_jogadores
            else:
                print('Por favor, digite um número entre 1 e 5 jogadores!')
        except ValueError:
            print('Entrada inválida')


def cria_bingo_aleatorio(lin: int, col: int) -> list:
    """
    Cria uma matriz para representar uma cartela de Bingo, preenchendo-a com números aleatórios sem repetição.

    Args:
        lin (int): O número de linhas da cartela.
        col (int): O número de colunas da cartela.

    Returns:
        list: Uma matriz representando a cartela de Bingo preenchida com números aleatórios.
    """

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

def sorteia_numero(lista: list) -> list:
    """
    Sorteia um número aleatório no intervalo de 1 a 50 que ainda não foi sorteado.

    Args:
        lista (list): Uma lista de números já sorteados.

    Returns:
        list: A lista de números atualizada após o novo sorteio.
    """
    input("Pressione ENTER para sortear...")
    verifica = lista
    n_sort = 0
    while n_sort == 0 or n_sort in verifica:
        n_sort = randint(1,50)
    lista.append(n_sort)
    print(f'Numero sorteado: {n_sort}')
    return(lista)
    
    

def exibe_matriz(matriz: list) -> None:
    """
    Exibe a matriz no console.

    Args:
        matriz (list): A matriz a ser exibida.

    Returns:
        None
    """
    print()
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()
    print()
    

def solicita_nomes(num_jogadores: int) -> list:
    """
    Solicita o nome dos jogadores e retorna uma lista com os nomes.

    Args:
        num_jogadores (int): O número de jogadores.

    Returns:
        list: Uma lista contendo os nomes dos jogadores.
    """
    nomes_jogadores = []
    for i in range(num_jogadores):
        nome = input(f'Nome do {i + 1}º jogador: ')
        while nome == '':
            nome = input(f'Nome do {i + 1}º jogador: ')
        nomes_jogadores.append(nome)
    return nomes_jogadores



def main() -> None:
    """
    Função principal que controla o jogo de Bingo, incluindo a criação das cartelas, sorteio de números e
    determinação do vencedor.

    Returns:
        None
    """
    resposta = 1
    vitorias = {}
    while resposta != 0:    
        qtd_jogadores = inicio_de_jogo()
        nomes_jogadores = solicita_nomes(qtd_jogadores)
        

        jogos = []
        for jogador in nomes_jogadores:
            print(f'Jogador {nomes_jogadores.index(jogador) + 1}: {jogador}')
            cartela = cria_bingo_aleatorio(5,5)
            jogos.append(cartela)
            exibe_matriz(jogos[nomes_jogadores.index(jogador)])

        status = True
        vencedor = None
            
            
        while status:
            lista_num_sorteados = []
            lista_num_sorteados = sorteia_numero(lista_num_sorteados)

            for cartela in jogos:
                for i in range(len(cartela)):
                    for j in range(len(cartela[0])):
                        if cartela[i][j] == lista_num_sorteados[-1]:
                            cartela[i][j] = 'XX'

            for i in range(qtd_jogadores):
                exibe_matriz(jogos[i])
                print('---------------------------')

            for cartela in jogos:
                for i in range(len(cartela)):
                    if cartela[0][0] == cartela[0][1] == cartela[0][2] == cartela[0][3] == cartela[0][4] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[1][0] == cartela[1][1] == cartela[1][2] == cartela[1][3] == cartela[1][4] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[2][0] == cartela[2][1] == cartela[2][2] == cartela[2][3] == cartela[2][4] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[3][0] == cartela[3][1] == cartela[3][2] == cartela[3][3] == cartela[3][4] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[4][0] == cartela[4][1] == cartela[4][2] == cartela[4][3] == cartela[4][4] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[0][0] == cartela[1][0] == cartela[2][0] == cartela[3][0] == cartela[4][0] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[0][1] == cartela[1][1] == cartela[2][1] == cartela[3][1] == cartela[4][1] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[0][2] == cartela[1][2] == cartela[2][2] == cartela[3][2] == cartela[4][2] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[0][3] == cartela[1][3] == cartela[2][3] == cartela[3][3] == cartela[4][3] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[0][4] == cartela[1][4] == cartela[2][4] == cartela[3][4] == cartela[4][4] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[0][0] == cartela[1][1] == cartela[2][2] == cartela[3][3] == cartela[4][4] == 'XX':
                        vencedor = jogos.index(cartela)
                    elif cartela[0][4] == cartela[1][3] == cartela[2][2] == cartela[3][1] == cartela[4][0] == 'XX':
                        vencedor = jogos.index(cartela)
            if vencedor is not None:
                print(f'Jogador: {nomes_jogadores[vencedor]} Venceu!')
                vitorias[nomes_jogadores[vencedor]] = vitorias.get(nomes_jogadores[vencedor], 0) + 1
                status = False
                

            
        print('Jogo encerrado!')
        with open('ranking.txt','w') as arquivo:
            for item in vitorias:
                arquivo.write(f'{item} {vitorias[item]}\n')
        resposta = int(input('Deseja jogar novamente? Digite 1 para sim e 0 para não: '))
    print(f'FIM DE PROGRAMA - Ranking: {vitorias} ')

main()