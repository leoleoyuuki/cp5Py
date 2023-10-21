from random import randint
# def sorteia_numero():
#     sorteio_bindo = []
#     nb = randint(1, 51)
#     while nb in sorteio_bindo:
#         nb = randint(1, 50)
#     sorteio_bindo.append(nb)
#     return sorteio_bindo
# print(sorteia_numero)

def sorteia_numero(sorteio_bingo):
    sorteio_bingo = [] 
    nb = randint(1, 50)
    while nb in sorteio_bingo:
        nb = randint(1, 50)
    sorteio_bingo.append(nb)
    return sorteio_bingo

sorteio_bingo = sorteia_numero()
print(sorteio_bingo)