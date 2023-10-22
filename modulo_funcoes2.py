from random import randint
#começo do jogo onde pede numero de jogadores e nome até verificação de vitoria
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

def cria_matriz_vazia():
    cartela = [[0] * 5 for i in range(5)]
    return cartela

def cria_matriz_para_jogadores(nomes_jogadores):
    cartelas = {nome: cria_matriz_vazia() for nome in nomes_jogadores}
    return cartelas

def exibe_cartela(cartela):
    for linha in cartela:
        for elemento in linha:
            print(elemento, end='\t')
        print()

def exibe_cartelas_atualizadas(cartelas_jogadores):
    for nome, cartela in cartelas_jogadores.items():
        print(f"Cartela de {nome}:")
        exibe_cartela(cartela)

def verifica_vitoria(cartela):
    # Verifica linhas
    for linha in cartela:
        if all(item == 'X' for item in linha):
            return True

    # Verifica colunas
    for coluna in range(5):
        if all(cartela[i][coluna] == 'X' for i in range(5)):
            return True

    return False

def marca_numero_na_cartela(cartela, jogador, linha, coluna):
    if 0 <= linha < 5 and 0 <= coluna < 5 and cartela[linha][coluna] == 0:
        cartela[linha][coluna] = 'X'
        return True
    else:
        return False

def marca_numeros_jogadores(cartelas_jogadores):
    vencedor = None

    while vencedor is None:
        for nome, cartela in cartelas_jogadores.items():
            print(f"É a vez de {nome}.")
            print(f"Cartela de {nome}:")
            exibe_cartela(cartela)
            
            while True:
                linha = int(input("Digite a linha (0 a 4) onde deseja marcar (X): "))
                coluna = int(input("Digite a coluna (0 a 4) onde deseja marcar (X): "))
                
                if marca_numero_na_cartela(cartela, nome, linha, coluna):
                    print(f"{nome} marcou (X) na linha {linha}, coluna {coluna}.")
                    exibe_cartelas_atualizadas(cartelas_jogadores)
                    
                    if verifica_vitoria(cartela):
                        vencedor = nome
                        break
                    else:
                        break
                else:
                    print("Posição inválida ou já marcada. Tente novamente.")

    print(f'{vencedor} venceu o jogo!')

nm_jogadores = inicio_de_jogo()
print(f'Número de jogadores: {nm_jogadores}')

# Teste da função solicita_nomes
nomes_jogadores = solicita_nomes(nm_jogadores)
print('Nomes dos jogadores:')
for i, nome in enumerate(nomes_jogadores):
    print(f'Jogador {i + 1} - {nome}')

cartelas_jogadores = cria_matriz_para_jogadores(nomes_jogadores)

# Iniciar o jogo, permitindo que cada jogador marque números em sua cartela
marca_numeros_jogadores(cartelas_jogadores)



#começo do jogo onde pede numero de jogadores e nome

#começo do bingo
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
#final das tabelas bingo

#sorteio de numeros para o bingo
def sorteia_numero(sorteio_bingo):
    sorteio_bingo = set()
    while len(sorteio_bingo) < 50:
        input("Pressione Enter para sortear um número...")
        sorteia_bingo = randint(1, 50)
        while sorteio_bingo in sorteio_bingo:
            sorteia_bingo = randint(1, 50)
        sorteio_bingo.add(sorteia_bingo)
        print(f"Número sorteado: {sorteia_bingo}")

sorteio_bingo = set()
sorteia_numero(sorteio_bingo)

#sorteio de numeros para o bingo


