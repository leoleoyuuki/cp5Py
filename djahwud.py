from random import randint
# def sorteia_numero():
#     sorteio_bindo = []
#     nb = randint(1, 51)
#     while nb in sorteio_bindo:
#         nb = randint(1, 50)
#     sorteio_bindo.append(nb)
#     return sorteio_bindo
# print(sorteia_numero)

# def sorteia_numero(sorteio_bingo):
#     sorteio_bingo = set()
#     while len(sorteio_bingo) < 50:
#         input("Pressione Enter para sortear um número...")
#         sorteia_bingo = randint(1, 50)
#         while sorteio_bingo in sorteio_bingo:
#             sorteia_bingo = randint(1, 50)
#         sorteio_bingo.add(sorteia_bingo)
#         print(f"Número sorteado: {sorteia_bingo}")

# sorteio_bingo = set()
# sorteia_numero(sorteio_bingo)


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
print(f'Número de jogadores: {nm_jogadores}')

# Teste da função solicita_nomes
nomes_jogadores = solicita_nomes(nm_jogadores)
print('Nomes dos jogadores:')
for i, nome in enumerate(nomes_jogadores):
    print(f'Jogador {i + 1} - {nome}')

def cria_matriz_vazia():
    cartela =[[0]*5 for i in range(5)]
    return cartela

def cria_matriz_para_jogadores(nomes_jogadores):
    cartelas = {nome: cria_matriz_vazia() for nome in nomes_jogadores}
    return cartelas

cartelas_jogadores = cria_matriz_para_jogadores(nomes_jogadores)

def exibe_cartela(cartela):
    for linha in cartela:
        for elemento in linha:
            print(elemento, end='\t')
        print()

for nome, cartela in cartelas_jogadores.items():
    print(f"Cartela de {nome}:")
    exibe_cartela(cartela)

def marca_numero_na_cartela(cartela, linha, coluna):
    if 0 <= linha < 5 and 0 <= coluna < 5 and cartela[linha][coluna] == 0:
        cartela[linha][coluna] = 'X'
        return True
    else:
        return False

def marca_numero_na_cartela(cartela, linha, coluna):
    if 0 <= linha < 5 and 0 <= coluna < 5 and cartela[linha][coluna] == 0:
        cartela[linha][coluna] = 'X'
        return True
    else:
        return False

# Função para marcar números nas cartelas dos jogadores
def marca_numeros_jogadores(cartelas_jogadores):
    for nome, cartela in cartelas_jogadores.items():
        print(f"É a vez de {nome}.")
        linha = int(input("Digite a linha (0 a 4) onde deseja marcar (X): "))
        coluna = int(input("Digite a coluna (0 a 4) onde deseja marcar (X): "))
        if marca_numero_na_cartela(cartela, linha, coluna):
            print(f"{nome} marcou (X) na linha {linha}, coluna {coluna}.")
        else:
            print("Posição inválida ou já marcada. Tente novamente.")

cartelas_jogadores = cria_matriz_para_jogadores(nomes_jogadores)


marca_numeros_jogadores(cartelas_jogadores)